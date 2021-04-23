from django.urls import path,include
from invent.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('crud',views.ClientInvent,basename='client')

urlpatterns = [
    path('',include(router.urls))
]