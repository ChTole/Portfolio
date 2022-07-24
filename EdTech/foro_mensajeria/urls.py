from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    path('foro/list', views.ForoList.as_view(), name='foro-list'),
    path('posteo/<pk>', views.ForoDetail.as_view(), name='Detail'),
]