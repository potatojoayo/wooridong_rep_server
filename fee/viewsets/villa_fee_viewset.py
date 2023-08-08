from rest_framework import viewsets

from ..serializers import VillaFeeSerializer, VillaFeeCreateSerializer
from ..models import VillaFee
from ..filters import VillaFeeFilter


class VillaFeeViewSet(viewsets.ModelViewSet):
    filterset_class = VillaFeeFilter

    def get_serializer_class(self):
        if self.action == 'update' or self.action == 'create' or self.request.method == 'PATCH':
            return VillaFeeCreateSerializer
        return VillaFeeSerializer

    def get_queryset(self):
        self.request.user.villa.get()
        return VillaFee.objects.filter(villa=self.request.user.villa.get()).order_by('pk')

    def partial_update(self, request, *args, **kwargs):

        kwargs['partial'] = True
        instance = self.get_object()

        fee = request.data.get('fee')
        # VillaFee 요금 변경 시 UnitBill, UnitFee 업데이트
        if fee is not None:
            instance.fee = int(fee)
            from fee.methods import update_fee_when_villa_fee_changes
            update_fee_when_villa_fee_changes(instance)
        print(1)
        print(request)
        return self.update(request, *args, **kwargs)
