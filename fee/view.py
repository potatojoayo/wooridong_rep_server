from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from villa.models import Unit,Villa
from villa.serializers import UnitSerializer, VillaNoDepthSerializer

class UnitBillToSend(APIView):

    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request, format=None):

        unit_id = request.query_params['unit']
        unit = Unit.objects.get(pk=unit_id)

        
        unit_serializer = UnitSerializer(unit)
        villa_serializer = VillaNoDepthSerializer(unit.villa)
        return Response(villa_serializer.data)
        



