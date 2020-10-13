import requests
import xmltodict
import json


class SQM(object):

    url = "https://ei.mci.local/services/FeedService.FeedServiceHttpsSoap11Endpoint"


    def get_event_by_cell(self,cell_name):
        """
        cell_name     is string with comma delimiter of cell name example : TH1G5454,THasd12
        :param cell_name:
        :return:
        """
        event_id = 0
        # headers = {'content-type': 'application/soap+xml'}
        headers = {'content-type': 'text/xml', 'SOAPAction': 'smartRoad_addEvent'}
        body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:def="http://DefaultNamespace">
          <soapenv:Header/>
          <soapenv:Body>
             <def:smartRoad_addEvent>
                <def:CellName>%s</def:CellName>
                <def:Token>eyJhbGciO.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZX</def:Token>
             </def:smartRoad_addEvent>
          </soapenv:Body>
       </soapenv:Envelope>""" % cell_name
        try:
            response = requests.post(self.url, data=body, headers=headers, verify=False)
            temp = xmltodict.parse(response.content)["soapenv:Envelope"]["soapenv:Body"]["smartRoad_addEventResponse"][
                "smartRoad_addEventReturn"]
            temp_1 = json.loads(temp)
            for i in temp_1:
                event_id = int(i)
        except NameError:
            return None

        return event_id


    def get_mobile_event(self,event_id):
        result = []

        # headers = {'content-type': 'application/soap+xml'}
        headers = {'content-type': 'text/xml', 'SOAPAction': 'smartRoad_retriveSubscriberByEvent'}
        body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:def="http://DefaultNamespace">
          <soapenv:Header/>
          <soapenv:Body>
             <def:smartRoad_retriveSubscriberByEvent>
                <def:EventID>%s</def:EventID>
                <def:Token>eyJhbGciO.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZX</def:Token>
             </def:smartRoad_retriveSubscriberByEvent>
          </soapenv:Body>
       </soapenv:Envelope>""" % event_id

        response = requests.post(self.url, data=body, headers=headers, verify=False)
        # print(response.content)
        numbers = \
        xmltodict.parse(response.content)["soapenv:Envelope"]["soapenv:Body"]["smartRoad_retriveSubscriberByEventResponse"][
            "smartRoad_retriveSubscriberByEventReturn"]

        for i in json.loads(numbers):
            result.append(i)
        return result
