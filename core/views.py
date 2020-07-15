from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from core.models import MciArea


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

        return render(request, self.template_name,
                      { })

class service_2(View):
    template_name="core/map2.html"
    def get(self,request):
        mci_area =MciArea.objects.filter()
        return render(request, self.template_name,
                      {"mci_area":mci_area })

class service_sms(View):
    template_name="core/service_sms.html"
    def get(self,request):
        mci_area =MciArea.objects.filter()
        return render(request, self.template_name,
                      {"mci_area":mci_area })