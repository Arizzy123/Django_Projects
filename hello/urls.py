
from django.urls import path
from hello.views import display
from hello.views import displaydatetime




urlpatterns=[
    path('hello/', display),
    path('datetime/',displaydatetime),
   
]