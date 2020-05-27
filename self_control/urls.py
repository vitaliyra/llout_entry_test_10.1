from django.urls import path
from . import views

app_name = 'self_control'

urlpatterns	=	[

path('', views.index, name='home'),
path('post', views.index_post, name='home_post'),
]
