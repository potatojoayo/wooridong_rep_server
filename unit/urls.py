from django.urls import path

from unit.views import detail_view

urlpatterns = [
    path('detail/<unit_bill_id>/', detail_view, name='detail', ),
]
