from django.urls import path
#from . import views
from .views import InferenceAPI, TestAPI

urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path("inference/", InferenceAPI),
    path("test/", TestAPI),

]