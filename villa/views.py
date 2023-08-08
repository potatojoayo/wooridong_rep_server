import requests
import json

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from bank.models import Bank
from user.models import User
from villa.models import Villa
from villa.models.rep_take_over import RepTakeOver


class ListAddress(APIView):

    def get(self, request, format=None):
        keyword = request.query_params['keyword']
        params = {
            'confmKey': 'U01TX0FVVEgyMDIyMDMyMzExNDQwNTExMjM3NTQ=',
            'currentPage': '1',
            'countPerPage': '100',
            'keyword': keyword,
            'resultType': 'json'
        }
        response = requests.get('https://www.juso.go.kr/addrlink/addrLinkApiJsonp.do', params=params)
        data = json.loads(response.content[1:-1])

        return Response(data, status=status.HTTP_200_OK)


class ListAddressDetail(APIView):

    def get(self, request, format=None):
        admCd = request.query_params['admCd']
        rnMgtSn = request.query_params['rnMgtSn']
        udrtYn = request.query_params['udrtYn']
        buldMnnm = request.query_params['buldMnnm']
        buldSlno = request.query_params['buldSlno']
        dongNm = request.query_params.get('dongNm')
        searchType = request.query_params.get('searchType')

        params = {
            'confmKey': 'U01TX0FVVEgyMDIyMDMyMzExMzg0MzExMjM3NTM=',
            'admCd': admCd,
            'rnMgtSn': rnMgtSn,
            'udrtYn': udrtYn,
            'buldMnnm': buldMnnm,
            'buldSlno': buldSlno,
            'resultType': 'json',
            'dongNm': dongNm,
            'searchType': searchType,
        }
        response = requests.get('https://www.juso.go.kr/addrlink/addrDetailApi.do', params=params)
        data = json.loads(response.content)
        print(data)

        return Response(data, status=status.HTTP_200_OK)


class ChangeVillaRep(APIView):

    def post(self, request):
        print('11')
        user = User.objects.filter(pk=self.request.data['rep_id'])
        Villa.objects.filter(pk=self.request.data['villa_id']).update(rep_id=self.request.data['rep_id'])
        villa = Villa.objects.filter(pk=self.request.data['villa_id'])
        RepTakeOver.objects.filter(villa_id=villa.get().id).update(is_takeover=True,current_user_id=self.request.data['rep_id'])
        data = list(villa.values())
        return Response(data, status=status.HTTP_200_OK)


@api_view(['PATCH'])
def update_bank(request: Request):
    villa: Villa = request.user.villa.get()
    data = request.data
    bank_id = data.get('bank')
    bank_account = data.get('bank_account')
    account_owner = data.get('account_owner')
    if bank_id:
        bank = Bank.objects.get(pk=bank_id)
        villa.bank = bank
    if bank_account:
        villa.bank_account = bank_account
    if account_owner:
        villa.account_owner = account_owner
    villa.save()

    return Response(200,)


