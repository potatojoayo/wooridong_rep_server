from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.send_bill_to_all_units import send_bills_to_all_units
from .views.send_bill import send_bills
from .viewsets import BillMessageViewSet ,UserVerificationMessageViewSet, RepVerificationMessageViewSet, AnnouncementMessageViewSet, InterimSettlementMessageViewSet

router = DefaultRouter()

router.register('bill-message',BillMessageViewSet,'bill_message')
router.register('announcement-message',AnnouncementMessageViewSet,'announcement_message')
router.register('user-verification-message', UserVerificationMessageViewSet, basename='user_verification_message')
router.register('rep-verification-message', RepVerificationMessageViewSet, basename='rep_verification_message')
router.register('interim-settlement-message', InterimSettlementMessageViewSet, basename='interim_settlement_message')


urlpatterns = [
    path('send-bills-to-all/', send_bills_to_all_units),
    path('send-bill/', send_bills),
    path('',include(router.urls)),
]
