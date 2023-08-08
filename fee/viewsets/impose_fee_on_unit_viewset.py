from rest_framework import viewsets
from ..serializers import ImposeFeeOnUnitSerializer , ImposeFeeOnUnitCreateSerializer
from datetime import datetime
from ..models import ImposeFeeOnUnit
from ..filters import ImposeFeeOnUnitFilter


class ImposeFeeOnUnitViewSet(viewsets.ModelViewSet):

    serializer_class = ImposeFeeOnUnitSerializer 
    filterset_class = ImposeFeeOnUnitFilter

    def get_serializer_class(self):
        if self.action == 'update' or self.action == 'create':
            return ImposeFeeOnUnitCreateSerializer
        return ImposeFeeOnUnitSerializer

    def get_queryset(self):
        return ImposeFeeOnUnit.objects.filter(villa=self.request.user.villa.get())

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        instance: ImposeFeeOnUnit = self.get_object()
        villa_fee = instance.villa_fee

        # do_impose 를 변경할 시
        if instance.do_impose != request.data['do_impose']:
            # do_impose 를 True로 바꿀 시
            if request.data['do_impose']:
                villa_fee.imposing_unit_count += 1
                if instance.unit.person_count is not None:
                    villa_fee.imposing_person_count += instance.unit.person_count 
            else:
                villa_fee.imposing_unit_count -= 1
                if instance.unit.person_count is not None:
                    villa_fee.imposing_person_count -= instance.unit.person_count 
            villa_fee.save()
            instance.do_impose = request.data['do_impose']
            instance.save()
            from fee.methods import update_fee_when_villa_fee_changes
            update_fee_when_villa_fee_changes(villa_fee=villa_fee)

        return super(ImposeFeeOnUnitViewSet, self).partial_update(request, *args, **kwargs)


            

