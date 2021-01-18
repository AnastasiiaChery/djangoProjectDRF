from django.urls import path
from .views import MyApiView, ReadUpdateView

urlpatterns = [
path('', MyApiView.as_view(), name='myapiview'),
path('/<int:id>', ReadUpdateView.as_view(), name='readUpdate')
]