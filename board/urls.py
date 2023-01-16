from django.urls import path

from .views import (
    AdList,
    AdDetail,
)

urlpatterns = [
    path('', AdList.as_view(), name='ad_list'),
    path('<int:pk>', AdDetail.as_view(), name='ad_details'),
]
