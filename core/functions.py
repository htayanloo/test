import json

from pip._vendor import urllib3


def get_station_list(self):
    http = urllib3.PoolManager()
    data = {'barcode': "barcode"}
    # data = {'barcode': barcode,"national_code":national_code}
    encoded_data = json.dumps(data).encode('utf-8')
    # r = http.request('POST','http://toosheh.tapin.ir/api/v1/track/',body = encoded_data,headers = {'Content-Type': 'application/json'})
    r = http.request('GET', 'http://gw.mci.local/AirGetStation/v1', body=encoded_data,
                     headers={'Content-Type': 'application/json'})

    if r.status != 200:
        return {"status": False, "detail": None}
    else:

        temp_json = json.loads(r.data.decode('utf-8'))

        return {"status": True, "detail": json.loads(r.data.decode('utf-8'))}


def get_station_detail(self):
    http = urllib3.PoolManager()
    data = {
  "DateFrom": "06/02/2020 10:00",
  "DateTo": "06/03/2020 10:00",
  "StationId": 0

}
    # data = {'barcode': barcode,"national_code":national_code}
    encoded_data = json.dumps(data).encode('utf-8')
    # r = http.request('POST','http://toosheh.tapin.ir/api/v1/track/',body = encoded_data,headers = {'Content-Type': 'application/json'})
    r = http.request('POST', 'http://gw.mci.local/AQI/v1', body=encoded_data,
                     headers={'Content-Type': 'application/json'})

    if r.status != 200:
        return {"status": False, "detail": None}
    else:

        temp_json = json.loads(r.data.decode('utf-8'))

        return {"status": True, "detail": json.loads(r.data.decode('utf-8'))}


def send_sms(cd):
    http = urllib3.PoolManager()
    data =  {
     "phone_number": cd["receptor"],
     "message": cd["message"],
     "method":"ht"
 }
    # data = {'barcode': barcode,"national_code":national_code}
    encoded_data = json.dumps(data).encode('utf-8')
    r = http.request('POST', 'http://ei.mci.local/Services/SendSms', body=encoded_data,
                     headers={'Content-Type': 'application/json'})
    print(r.status)
    if r.status != 200:
        return {"status": False, "detail": None}
    else:

        temp_json = json.loads(r.data.decode('utf-8'))

        return {"status": True, "detail": json.loads(r.data.decode('utf-8'))}