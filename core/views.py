from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View

from core.forms import Notify, gas_co2_alert
from core.functions import get_station_list, get_station_detail, send_sms
from core.models import MciArea, MushroomSpot, alert, Receptor


class Login(View):
    template_name = "core/login.html"

    def get(self, request):
        form = ""
        return render(request, self.template_name,
                      {'search_form': form})

    def post(self, request):
        form = ""
        return redirect('service_1')


class Dashboard(View):
    template_name = "core/dashboard.html"

    def get(self, request):
        form = ""
        return render(request, self.template_name,
                      {})


class Map(View):
    template_name = "core/map.html"

    def get(self, request):
        form = ""
        return render(request, self.template_name,
                      {})


class service_1(View):
    template_name = "core/map1.html"

    def get(self, request):
        #station_list = get_station_list("as")
        station_list={"status": False, "detail": [
            {"StationId":1,"Longitude":51.448187,"Latitude":35.744257, ,"AQI":10,"StationName_Fa":"ایستگاه یک"},
        {"StationId": 2, "Longitude": 51.493105, "Latitude": 35.757731, "AQI": 14, "StationName_Fa": "ایستگاه دو"},
        {"StationId": 3, "Longitude": 51.320125, "Latitude": 35.727770, "AQI": 1, "StationName_Fa": "ایستگاه سه"},
        {"StationId": 4, "Longitude": 51.368833, "Latitude": 35.770709, "AQI": 101, "StationName_Fa": "ایستگاه چهار"},
        {"StationId": 5, "Longitude": 51.452613, "Latitude": 35.751773, "AQI": 145, "StationName_Fa": "ایستگاه پنج"},
        ]}
        form = gas_co2_alert
        return render(request, self.template_name,
                      {"station_list": station_list, "form": form})

    def post(self, request):
        message = ""
        station_list = station_list={"status": False, "detail": [
            {"StationId":1,"Longitude":51.448187,"Latitude":35.744257, ,"AQI":10,"StationName_Fa":"ایستگاه یک"},
        {"StationId": 2, "Longitude": 51.493105, "Latitude": 35.757731, "AQI": 14, "StationName_Fa": "ایستگاه دو"},
        {"StationId": 3, "Longitude": 51.320125, "Latitude": 35.727770, "AQI": 1, "StationName_Fa": "ایستگاه سه"},
        {"StationId": 4, "Longitude": 51.368833, "Latitude": 35.770709, "AQI": 101, "StationName_Fa": "ایستگاه چهار"},
        {"StationId": 5, "Longitude": 51.452613, "Latitude": 35.751773, "AQI": 145, "StationName_Fa": "ایستگاه پنج"},
        ]}

        form = gas_co2_alert(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                temp = alert.objects.get(key="co")
            except:
                temp = alert.objects.create(key="co", value=cd["co"])
                message = "با موفقیت بروز رسانی شد"
            else:

                temp.value = cd["co"]
                temp.save()
                message = "با موفقیت بروز رسانی شد"

        return render(request, self.template_name,
                      {"station_list": station_list, "form": form, "message": message})


class service_2(View):
    template_name = "core/map2.html"

    def get(self, request):
        mci_area = MushroomSpot.objects.filter()
        station_list = station_list={"status": False, "detail": [
            {"StationId":1,"Longitude":51.448187,"Latitude":35.744257, ,"AQI":10,"StationName_Fa":"ایستگاه یک"},
        {"StationId": 2, "Longitude": 51.493105, "Latitude": 35.757731, "AQI": 14, "StationName_Fa": "ایستگاه دو"},
        {"StationId": 3, "Longitude": 51.320125, "Latitude": 35.727770, "AQI": 1, "StationName_Fa": "ایستگاه سه"},
        {"StationId": 4, "Longitude": 51.368833, "Latitude": 35.770709, "AQI": 101, "StationName_Fa": "ایستگاه چهار"},
        {"StationId": 5, "Longitude": 51.452613, "Latitude": 35.751773, "AQI": 145, "StationName_Fa": "ایستگاه پنج"},
        ]}
        return render(request, self.template_name,
                      {"mci_area": mci_area, "station_list": station_list})


class service_sms(View):
    template_name = "core/service_sms.html"

    def get(self, request):
        mci_area = MciArea.objects.filter()
        message=""
        if request.GET["service"]=="2":
            message = "در محدوده شما زلزله رخ داده است لطفا اقدامات لازم جهت سلامت خود و خانواده خود انجام دهید"
        elif request.GET["service"] == "1":
            message = "آلودگی هوا در محدوده شما بیش از حد مجاز میباشد"


        form = Notify(initial={"message":message})
        receptor = Receptor.objects.filter(area=request.GET["id"])



        return render(request, self.template_name,
                      {"mci_area": mci_area, "form": form, "receptor": receptor})

    def post(self, request):
        message = ""
        form = Notify(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            temp = send_sms(cd)
            print(temp)
            if temp["status"]:
                message = "پیام با موفقیت ارسال شد"
            else:
                message = "ارسال پیام با مشکل مواجه شد"

        if request.GET["service"]=="2":
            message1 = "در محدوده شما زلزله رخ داده است لطفا اقدامات لازم جهت سلامت خود و خانواده خود انجام دهید"
        elif request.GET["service"] == "1":
            message1 = "آلودگی هوا در محدوده شما بیش از حد مجاز میباشد"
        for i in Receptor.objects.filter(area=request.GET["id"]):
            send_sms({"receptor": i.mobile, "message": message1})
        return render(request, self.template_name,
                      {"form": form, "message": message})


class service_cron(View):
    template_name = "core/service_sms.html"

    def get(self, request):
        temp = alert.objects.filter(key="co")
        print(temp[0].value)
        station_detail = get_station_detail(1)
        print(station_detail["detail"][0]["co"])
        if float(station_detail["detail"][0]["co"])>float(temp[0].value):
            for i in Receptor.objects.filter(area=1):
                send_sms({"receptor":i.mobile,"message":"اعلام وضعیت هشدار بصورت اتوماتیک"})

        return render(request, self.template_name,
                      {})
