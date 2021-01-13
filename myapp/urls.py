from django.urls import path
from .views import MyApiView

urlpatterns = [
path('', MyApiView.as_view(), name='myapiview')
]