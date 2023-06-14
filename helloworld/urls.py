from django.urls import path
from . import views

urlpatterns = [
    path('Hello World',views.helloworld),
    path('HtmlDemo',views.Demohtml),
    path('Login',views.logindemo),
    path('verify',views.verifydata),
    path('demoData',views.demoData),
    path('demoData1',views.demoData1)
]
