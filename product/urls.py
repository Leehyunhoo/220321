from django.urls import path
#from . import views
from .views import GetTrainData, TestAPI

urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path("gettraindata/", GetTrainData),
    path("test/", TestAPI),

]