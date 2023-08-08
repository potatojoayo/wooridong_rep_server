from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView

from rest_framework.routers import DefaultRouter

from server import settings
from villa.viewsets import BuildingViewSet, UnitViewSet, UnitWithBillViewSet, WebDetailUnitViewSet, UnitAllowAnyViewSet
from user.viewsets import UserViewSet, UserAllowAnyViewSet

router = DefaultRouter()
router.register('building', BuildingViewSet, basename='building')
router.register('unit', UnitViewSet, basename='unit')
router.register('unit/allow-any', UnitAllowAnyViewSet, basename='unit_allow_any')
router.register('unit-with-bill', UnitWithBillViewSet, basename='unit_with_bill')
router.register('user/update', UserViewSet, basename='user')
router.register('user/allow-any', UserAllowAnyViewSet, basename='user_allow_any')
router.register('web-detail-unit', WebDetailUnitViewSet, basename='web_detail_unit')

urlpatterns = [
                  path('', include(router.urls)),
                  path('admin/', admin.site.urls),
                  path('user/', include('user.urls')),
                  path('web/unit/', include('unit.urls')),
                  path('bank/', include('bank.urls')),
                  path('villa/', include('villa.urls')),
                  path('message/', include('message.urls')),
                  path('fee/', include('fee.urls')),
                  path('notification/', include('notification.urls')),
                  path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
                  path("__reload__/", include("django_browser_reload.urls")),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
