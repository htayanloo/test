from django.shortcuts import render

# Create your views here.
from django.views import View

from core.ViewUtility import ViewUtility
from core.functions import send_sms, send_sms_direct, customer_location
from core.models import alert
from smart_road.forms import EventForm, CustomerNumber
from smart_road.models import Event
from smart_road.smartroad import SQM


class service_3(View, ViewUtility, SQM):
    template_name = "smart_road/service_3.html"
    form = EventForm

    def get(self, request):
        event_list = Event.objects.filter()
        items = self.pagination(request=request, list=event_list)

        return render(request, self.template_name,
                      {"items": items, "form": self.form})

    def post(self, request):
        message = ""

        form = self.form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            temp = form.save(commit=False)
            temp_cell = self.get_event_by_cell(temp.cell_name)
            print(temp_cell)
            if temp_cell:
                temp.event_id = temp_cell
                temp.save()

            message = "با موفقیت بروز رسانی شد"
        event_list = Event.objects.filter()
        items = self.pagination(request=request, list=event_list)

        return render(request, self.template_name,
                      {"items": items, "form": form, "message": message})


class service_3_sms(View, ViewUtility, SQM):
    template_name = "smart_road/service_3_sms.html"
    form = EventForm

    def get(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except:

            pass
        else:
            num_list = self.get_mobile_event(event.event_id)
            print(num_list)

            return render(request, self.template_name,
                          {"items": num_list, "form": self.form})

    def post(self, request, pk):
        message = ""
        try:
            event = Event.objects.get(pk=pk)
        except:

            pass
        else:
            message_list = ""
            num_list = self.get_mobile_event(event.event_id)
            for i in request.POST:
                if "checkbox-" in i:
                    message_list = message_list + ",0" + i[9:]
            print(message_list)
            temp = send_sms_direct(receptor=message_list, message=request.POST["text_message"])

            return render(request, self.template_name,
                          {"items": num_list, "form": self.form})


class service_4(View, ViewUtility, SQM):
    template_name = "smart_road/service_4.html"
    form = CustomerNumber

    def get(self, request):
        event_list = Event.objects.filter()
        items = self.pagination(request=request, list=event_list)

        mobile = {"mobile": "", "lat": "", "lng": "","base_lat": "35.700235", "base_lng": "51.382531",
                  "address":"","city":"","province":""}

        if "mobile" in request.GET:

            temp = customer_location(request.GET["mobile"])
            print(temp)
            lng =temp["detail"]["Result"]["Long"]
            lat =temp["detail"]["Result"]["Lat"]
            City =temp["detail"]["Result"]["City"]
            Province =temp["detail"]["Result"]["Province"]
            Site =temp["detail"]["Result"]["Site"]

            mobile = {"mobile":request.GET.get("mobile"),"lat":lat,"lng": lng,"city":City,"province":Province,"site":Site}

            temp_form = self.form(initial={"mobile":mobile["mobile"]})
        else:
            temp_form = self.form(initial={"mobile":""})
        return render(request, self.template_name,
                      {"items": items, "form": temp_form,"mobile":mobile})

    def post(self, request):
        message = ""

        form = self.form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            temp = form.save(commit=False)
            temp_cell = self.get_event_by_cell(temp.cell_name)
            print(temp_cell)
            if temp_cell:
                temp.event_id = temp_cell
                temp.save()

            message = "با موفقیت بروز رسانی شد"
        event_list = Event.objects.filter()
        items = self.pagination(request=request, list=event_list)

        return render(request, self.template_name,
                      {"items": items, "form": form, "message": message})
