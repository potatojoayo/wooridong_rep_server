from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .viewsets import VillaViewSet
from .views import ListAddress, ListAddressDetail, ChangeVillaRep, update_bank

router = DefaultRouter()
router.register('',VillaViewSet, basename='villa')

urlpatterns = [
    path('change-rep/', ChangeVillaRep.as_view()),
    path('address/',ListAddress.as_view()),
    path('address/detail/',ListAddressDetail.as_view()),
    path('update-bank/', update_bank),
    path('', include(router.urls)),
]
