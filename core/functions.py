import json
from datetime import datetime, timedelta

import requests
from pip._vendor import urllib3


def get_station_list(self):
    http = urllib3.PoolManager()
    data = {'barcode': "barcode"}
    # data = {'barcode': barcode,"national_code":national_code}
    encoded_data = json.dumps(data).encode('utf-8')
    # r = http.request('POST','http://toosheh.tapin.ir/api/v1/track/',body = encoded_data,headers = {'Content-Type': 'application/json'})
    #    r = http.request('GET', 'http://gw.mci.local/AirGetStation/v1', body=encoded_data, headers={'Content-Type': 'application/json'})
    r = http.request('GET', 'http://aqms.doe.ir/Home/LoadAQIMap?id=1&StateId=2', body=encoded_data,
                     headers={'Content-Type': 'application/json'})
    print(r.status)
    if r.status != 200:
        return {"status": False, "detail": []}
    else:

        temp_json = json.loads(r.data.decode('utf-8'))

        return {"status": True, "detail": json.loads(r.data.decode('utf-8'))}


def get_station_detail(stationid):
    http = urllib3.PoolManager()
    dateTimeObj = datetime.now()
    date_from = (dateTimeObj - timedelta(hours=0)).strftime("%m/%d/%Y %H:00")
    date_to = (dateTimeObj - timedelta(hours=0)).strftime("%m/%d/%Y %H:00")

    data = {
        "DateFrom": date_from,
        "DateTo": date_to,
        "StationId": stationid

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
    data = {
        "phone_number": str(cd["receptor"]),
        "message": cd["message"],
        "method": "ht"
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


def send_sms_direct(receptor, message):
    http = urllib3.PoolManager()

    # data = {'barcode': barcode,"national_code":national_code}
    #    message=message.encode('utf-8')

    r = requests.get(
        'https://api.kavenegar.com/v1/4935715544676C487076716636596E786554787531513D3D/sms/send.json?receptor=%s&sender=%s&message=%s' % (
        str(receptor), "10008663", message))
    # r = http.request('POST', 'https://api.kavenegar.com/v1/4935715544676C487076716636596E786554787531513D3D/sms/send.json?receptor=%s&sender=%s&message=%s' %(receptor,"10008663",message))
    print(r.status_code)
    if r.status_code != 200:
        return {"status": False, "detail": None}
    else:

        temp_json = json.loads(r.content.decode('utf-8'))

        return {"status": True, "detail": json.loads(r.content.decode('utf-8'))}
def send_sms_smpp(receptor, message):
    http = urllib3.PoolManager()
    data = {
        "receptor": receptor,
        "message": message,
    }
    # data = {'barcode': barcode,"national_code":national_code}
    encoded_data = json.dumps(data).encode('utf-8')
    r = http.request('POST', 'http://10.15.82.113:30760/smpp/flash/send', body=encoded_data,
                     headers={'Content-Type': 'application/json'})
    print(r.status)
    if r.status != 200:
        return {"status": False, "detail": None}
    else:

        temp_json = json.loads(r.data.decode('utf-8'))

        return {"status": True, "detail": json.loads(r.data.decode('utf-8'))}



def customer_location(mobile):
    http = urllib3.PoolManager()

    # data = {'barcode': barcode,"national_code":national_code}
    url_temp = "http://10.15.200.86:8080/sqmService/rest/srv/provideSubscriberInfo/security&Mcci9999&%s" % mobile
    r = http.request('GET', url_temp,headers={'Content-Type': 'application/json'})
    print(r.status)
    if r.status != 200:
        return {"status": False, "detail": None}
    else:

        temp_json = json.loads(r.data.decode('utf-8'))
        print(temp_json)

        return {"status": True, "detail": json.loads(r.data.decode('utf-8'))}


