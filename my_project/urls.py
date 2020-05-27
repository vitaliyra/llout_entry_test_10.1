from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), # new
    path('accounts/', include('django.contrib.auth.urls')),
    path('ll', TemplateView.as_view(template_name='home.html'), name='home'),
    #path('sc/', TemplateView.as_view(template_name="self_control/sc_in.html")),
    path('', include('firstapp.urls')),
    path('sc/', include('self_control.urls')),
    path('ent_test', include('entry_test.urls')),
]
