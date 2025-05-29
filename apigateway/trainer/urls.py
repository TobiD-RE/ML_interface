from django.urls import path
from .views import TrainModelProxyView

urlpatterns = [
    path('train/', TrainModelProxyView.as_view(), name='train-model'),
]