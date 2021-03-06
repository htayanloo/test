"""MCI_Demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from MCI_Demo import settings
from core.models import MushroomSpot
from core.views import Login, Dashboard,Map,service_1,service_2,service_sms,service_cron
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView

from smart_road.views import service_3, service_3_sms,service_4

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name='Login'),
    path('', Login.as_view(), name='Login'),
    path('panel/service/1/', service_1.as_view(), name='service_1'),
    path('panel/service/2/', service_2.as_view(), name='service_2'),
    path('panel/service/3/', service_3.as_view(), name='service_3'),
    path('panel/service/4/', service_4.as_view(), name='service_4'),
    path('panel/service/3/sms/<int:pk>/', service_3_sms.as_view(), name='service_3_sms'),
    path('panel/service/sms/', service_sms.as_view(), name='service_sms'),
    path('panel/service/sms/cron/', service_cron.as_view(), name='service_cron'),

    path('data.geojson/',GeoJSONLayerView.as_view(model=MushroomSpot, properties=('title', 'description', 'picture_url')), name='data')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)