from django.urls import path
from .views import boredAPIView

urlpatterns = [
    path('', boredAPIView, name='boredAPI'),
]
