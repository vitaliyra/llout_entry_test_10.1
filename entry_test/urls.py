from django.urls import path
from . import views

app_name = 'entry_test'

urlpatterns	=	[

path('', views.index, name='home'),
path('1', views.index1, name='home1'),
]
