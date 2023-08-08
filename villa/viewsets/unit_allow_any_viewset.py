from rest_framework.permissions import AllowAny
from rest_framework import viewsets 

from ..models import Unit
from ..serializers import UnitSerializer

class UnitAllowAnyViewSet(viewsets.ModelViewSet): 

    
    serializer_class = UnitSerializer 
    queryset = Unit.objects.all()
    permission_classes = [AllowAny]


    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        instance = self.get_object() 

        # 동대표 인증 변경 시
        rep = request.data.get('rep') 
        asked = request.query_params.get('asked')
        if rep != None:
            from notification.methods import create_notification
            print('yes')
            create_notification.change_rep_verification(asked=asked,new=rep,unit=instance) 


        return self.update(request, *args, **kwargs)
        

