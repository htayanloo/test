from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from core.forms import Notify
from core.functions import get_station_list, get_station_detail, send_sms
from core.models import MciArea, MushroomSpot


class Login(View):
    template_name="core/login.html"
    def get(self,request):
        form =""
        return render(request, self.template_name,
                      { 'search_form': form})


class Dashboard(View):
    template_name="core/dashboard.html"
    def get(self,request):
        form =""
        return render(request, self.template_name,
                      { })
class Map(View):
    template_name="core/map.html"
    def get(self,request):
        form =""
        return render(request, self.template_name,
                      { })


class service_1(View):
    template_name="core/map1.html"
    def get(self,request):
        station_list =get_station_list("as")
        station_detail =get_station_detail("as")
        for i in station_detail["detail"]:
            print(i)
        return render(request, self.template_name,
                      { "station_list": station_list})

class service_2(View):
    template_name="core/map2.html"
    def get(self,request):
        mci_area =MushroomSpot.objects.filter()
        return render(request, self.template_name,
                      {"mci_area":mci_area })

class service_sms(View):
    template_name="core/service_sms.html"
    def get(self,request):
        mci_area =MciArea.objects.filter()
        form = Notify()
        return render(request, self.template_name,
                      {"mci_area":mci_area,"form":form })
    def post(self,request):

        form = Notify(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            temp = send_sms(cd)
            print(temp)
        return render(request, self.template_name,
                      {"form":form })