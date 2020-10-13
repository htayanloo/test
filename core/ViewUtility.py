from django.core.mail import EmailMessage, BadHeaderError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template import Context
from django.template.loader import get_template



class ViewUtility(object):

    def __init__(self):
        pass

    def Alert_Generator(self, message, alert_type="success"):
        return """<div class="alert alert-%s alert-styled-left alert-arrow-left alert-bordered">
    										<button type="button" class="close" data-dismiss="alert"><span>×</span><span class="sr-only">Close</span></button>
    										<span class="text-semibold">%s</div>""" % (alert_type, message)

    def ActionMessageGenerate(self):
        request = self.request
        print(request.GET)

        if 'message' in self.request.GET:
            if request.GET['message'] == "404":
                self.message = self.Alert_Generator("Can not Found", alert_type="danger")
            elif request.GET['message'] == "200":
                self.message = self.Alert_Generator("Create success", alert_type="success")
            elif request.GET['message'] == "400":
                self.message = self.Alert_Generator("Create Fail", alert_type="danger")

    def pagination(self, request, list, count=10):
        paginator = Paginator(list, count)  # Show 25 contacts per page
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)

        contacts.object_list = self.addrow(contacts.object_list)

        return contacts

    def addrow(self, list):
        row = 1
        for item in list:
            item.row = row
            row += 1

        return list

    def GetFileNameTemplatePath(self, filename):
        return filename

    def numbers_to_letters(self, number):
        import re
        number = re.sub("\D", "", str(number))

        if number.__len__() > 12:
            raise ValueError('The length of number must be lower than 12')

        if int(number) == 0:
            return 'صفر ریال'
        if int(number) == 1000:
            return 'هزار ریال'

        ones_digit = ['صفر', 'یک', 'دو', 'سه', 'چهار', 'پنج', 'شش', 'هفت', 'هشت', 'نه']
        tens_digit = ['بیست', 'سی', 'چهل', 'پنجاه', 'شصت', 'هفتاد', 'هشتاد', 'نود']
        hundreds_digit = ['صد', 'دویست', 'سیصد', 'چهارصد', 'پانصد', 'ششصد', 'هفتصد', 'هشتصد', 'نهصد']
        eleven_to_nineteen = ['ده', 'یازده', 'دوازده', 'سیزده', 'چهارده', 'پانزده', 'شانزده', 'هفده', 'هجده', 'نوزده']
        postfixes = [' میلیارد', ' میلیون', ' هزار', '']


class VTEmail(object):

    def send(self, template, context, subject, to=[]):
        msg = EmailMessage(subject, self.generate(template=template, context=context), EMAIL_HOST_USER, to=to)
        msg.content_subtype = "html"
        msg.send()

    def generate(self, template, context):
        template = get_template('Base/email/' + template)
        content = template.render(context)
        return content

    def password_recovery_generate(self, user):
        hash = user.password_recovery_hash
        context = {'link': "%s/passworcrecovery/%s" %(BASE_URL,hash)}
        template = "password_recovery.html"
        to = ["htayanloo@gmail.com"]
        subject = "Test Email"
        self.send(template=template, context=context, subject=subject, to=to)
