from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import get_count_unpaid_unit_bills, get_count_unpaid_villa_fees, check_villa_fee_duplicated, \
    create_villa_fee, change_impose_type, unit_bills, create_unit_fee, change_do_impose
from .viewsets import ImposeFeeOnUnitViewSet, FeeTypeViewSet, VillaFeeViewSet, ImposeTypeViewSet, UnitFeeViewSet, \
    UnitBillViewSet, InterimSettlementViewSet
from .view import UnitBillToSend

router = DefaultRouter()

router.register('type', FeeTypeViewSet, 'fee_type')
router.register('impose-on-unit', ImposeFeeOnUnitViewSet, 'impose_fee_on_unit')
router.register('villa-fee', VillaFeeViewSet, 'villa_fee')
router.register('impose-type', ImposeTypeViewSet, 'impose_type')
router.register('unit-fee', UnitFeeViewSet, 'unit-fee')
router.register('unit-bill', UnitBillViewSet, 'unit-bill')
router.register('interim-settlement', InterimSettlementViewSet, 'interim_settlement')

urlpatterns = [
    path('unit-bill-to-send/', UnitBillToSend.as_view(), name='unit_bill_to_send'),
    path('unit-bill/unpaid/', get_count_unpaid_unit_bills),
    path('villa-fee/unpaid/', get_count_unpaid_villa_fees),
    path('villa-fee/check-duplicated/', check_villa_fee_duplicated),
    path('villa-fee/create/', create_villa_fee),
    path('villa-fee/change-impose-type/', change_impose_type),
    path('unit-bill/by-building/', unit_bills),
    path('unit-fee/create/', create_unit_fee),
    path('change-do-impose/', change_do_impose),

    path('', include(router.urls)),
]
