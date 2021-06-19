# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Guarantordetails, Applications, GuarantorLists, Guarantortosign
from django.shortcuts import render, get_object_or_404, redirect 
from django.http import HttpResponseRedirect, Http404, HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import F
from pprint import pprint
import requests
import json
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from weasyprint import HTML


def ping(request):
    return HttpResponse("00")

def index(request):
    guarantorlist = GuarantorLists.objects.raw('''SELECT b.ID, b.drn, b.lastname, b.firstname, b.phone, b.email, b.guarantorid, b.address, CONCAT(c.firstname, ' ', c.surname) AS drivername, d.requestid FROM guarantordetails b join applications c on b.DRN = c.DRN left join guarantortosign d on b.ID = d.guarantorid''')
    context = {
        'title': 'Welcome',
        'guarantorlist': guarantorlist,
    }
    return render(request, 'guarantordoc/index.html', context) 
    # return HttpResponse(guarantorlist)

def createDocument(fileList,Oauthtoken,guarantorname, guarantoremail):
    headers = {'Authorization':'Zoho-oauthtoken '+Oauthtoken}
    files =[]
    fs = FileSystemStorage('guarantordoc/unsigneddoc/')
    for i in fileList:
        files.append(('file', (i[0],fs.open(i[0]),i[2])))
    req_data={}
    req_data['request_name']=guarantorname
    req_data["expiration_days"]= 10
    req_data["is_sequential"]=True
    req_data["email_reminders"]=True
    req_data["reminder_period"]= 5
    actions_list=[]
    actions_list.append({"recipient_name":guarantorname,"recipient_email":guarantoremail,"action_type":"SIGN","private_notes":"Please get back to us for further queries","signing_order":0,"verify_recipient":False})
    req_data['actions']=actions_list
    data={}
    data['requests']=req_data
    data_json={}
    data_json['data'] = json.dumps(data)
    r = requests.post('https://sign.zoho.com/api/v1/requests', files=files, data=data_json,headers=headers)
    return r.json()
    
def submitDocument(request_id,respjson,Oauthtoken):
    headers = {'Authorization':'Zoho-oauthtoken '+Oauthtoken}
    req_data={}
    req_data['request_name']=respjson['request_name']
    docIdsJsonArray = respjson['document_ids']
    actionsJsonArray = respjson['actions']
    for i in docIdsJsonArray:
        docId=i["document_id"]      
        for j in actionsJsonArray:
            fields=[]
            sigField={}
            sigField["field_type_name"]= "Signature"
            sigField["is_mandatory"]= True
            sigField["field_name"]= "Signature"
            sigField["page_no"]= 0
            sigField["y_coord"]= 300
            sigField["abs_width"]= 305
            sigField["description_tooltip"]= ""
            sigField["x_coord"]= 60
            sigField["abs_height"]= 60
            sigField["document_id"]= docId
            fields.append(sigField)
            # emailField={}
            # emailField["field_type_name"]= "Textfield"
            # emailField["text_property"]={}
            # emailField["text_property"]["is_italic"]= False
            # emailField["text_property"]["is_underline"]= False
            # emailField["text_property"]["font_color"]= "000000"
            # emailField["text_property"]["font_size"]= 12
            # emailField["text_property"]["is_read_only"]= False
            # emailField["text_property"]["is_bold"]= False
            # emailField["text_property"]["font"]= "Arial"
            # emailField["is_mandatory"]= True
            # emailField["page_no"]= 0
            # emailField["document_id"]= docId
            # emailField["field_name"]= "In Year"
            # emailField["y_coord"]= 195
            # emailField["abs_width"]= 45
            # emailField["description_tooltip"]= ""
            # emailField["x_coord"]=350
            # emailField["abs_height"]= 16
            # fields.append(emailField)
            if 'fields' in j:
                j['fields']=j['fields']+fields
            else:
                j["fields"]=fields
            j.pop('is_bulk',None)
            j.pop('allow_signing',None)
            j.pop('action_status',None)
    req_data['actions']=actionsJsonArray
    data={}
    data['requests']=req_data
    data_json={}
    data_json['data'] = json.dumps(data)
    url = 'https://sign.zoho.com/api/v1/requests/'+request_id+'/submit'
    r = requests.post(url, files=[],data=data_json, headers=headers)
    return r.json()


def html_to_pdf_view(request, guarantorid):
    try:
        guarantor = Guarantordetails.objects.filter(id=guarantorid).only("firstname", "lastname","middlename", "phone", "email", "drn").first()
        driverdrn = guarantor.drn
        driver = Applications.objects.filter(drn=driverdrn).only("firstname", "surname","middlename", "mobile", "email", "drn").first()
        guarantorname = guarantor.firstname +" "+guarantor.lastname
        guarantoremail = guarantor.email
        
        docname = guarantor.firstname +""+guarantor.middlename+""+guarantor.lastname
        drivername = driver.firstname +" "+driver.middlename+" "+driver.surname
        
        html_string = render_to_string('guarantordoc/pdf_template.html', {'guarantorname': guarantorname, 'drivername': drivername})

        html = HTML(string=html_string)
        html.write_pdf(target='guarantordoc/unsigneddoc/'+docname+'.pdf');

        # return response
        # tokenjson = gettoken()
        refreshtokenjson = getrefreshtoken()
        
        Oauthtoken = refreshtokenjson['access_token']

        file_list=[[docname+".pdf","guarantordoc/unsigneddoc/","application/pdf"]]
        respjson= createDocument(file_list,Oauthtoken, guarantorname, guarantoremail)

        respjson=respjson['requests']
        request_id=respjson['request_id']
        submitrespjson=submitDocument(request_id,respjson,Oauthtoken)
        finalresp=submitrespjson['message']
        finalrespstatus=submitrespjson['status']
        # frequest_id=submitrespjson['request_id']

        guatosigndoc = Guarantortosign()
        guatosigndoc.guarantorid = guarantorid
        guatosigndoc.requestid = request_id
        guatosigndoc.status = "Pending"
        guatosigndoc.save()
        # fdocument_id=finalresp['document_ids']
        # return HttpResponse(finalresp)

        messages.success(request, finalresp+" to "+guarantorname)
        return HttpResponseRedirect('/guarantorslist/')
    except requests.exceptions.ConnectionError:
        connection_status = "Connection refused"
        context = {
            'exception': connection_status,
        }
        # return HttpResponse(requests.exceptions)
        messages.warning(request, connection_status)
        return HttpResponseRedirect('/guarantorslist/')
    except AssertionError as error:
        # Output expected AssertionErrors.
        # Logging.log_exception(error)
        context = {
            'exception': "Request Not found",
        }
        # return HttpResponse(error)
        messages.warning(request, error)
        return HttpResponseRedirect('/guarantorslist/')
    except Exception as exception:
        # Output unexpected Exceptions.
        # Logging.log_exception(exception, False)
        context = {
            'exception': "Request Not found",
        }
        # return HttpResponse(exception)
        messages.warning(request, exception)
        return HttpResponseRedirect('/guarantorslist/')

def gettoken_test(request):
    try:
        getresponse = requests.post('https://accounts.zoho.com/oauth/v2/token?refresh_token=1000.68e0e4370bdb84fc2b365aeff4c5fc65.d3dc0277456dddcb2df9ca8297d894ba&client_id=1000.2O5WF7FXABOWF8TRT4NVZ4GTDAUGOO&client_secret=6783e2b027b6c880b7dca0fe7a8d3762345ec76674&redirect_uri=http://127.0.0.1:8000/guarantors&grant_type=refresh_token')
        return HttpResponse(getresponse)
    except Exception as exception:
        context = {
            'exception': "Request Not found",
        }
        return HttpResponse(exception)

    
def gettoken():
    try:
        getresponse = requests.post('https://accounts.zoho.com/oauth/v2/token?code=1000.7f275cda053cc314d6d2353736087085.c542ce20f645dc531686d5fade9425e3&client_id=1000.61DFAE1NE31HICJJZC06O3EPY08W0V&client_secret=840dc61b265a5e413e2091d47c461a3af4324b314d&redirect_uri=https://guarantor.moove.africa/guarantors&grant_type=authorization_code')
        return getresponse.json()
    except Exception as exception:
        context = {
            'exception': "Request Not found",
        }
        return HttpResponse(exception)

def getrefreshtoken_test():
    try:
        getrefreshresponse = requests.post('https://accounts.zoho.com/oauth/v2/token?refresh_token=1000.68e0e4370bdb84fc2b365aeff4c5fc65.d3dc0277456dddcb2df9ca8297d894ba&client_id=1000.2O5WF7FXABOWF8TRT4NVZ4GTDAUGOO&client_secret=6783e2b027b6c880b7dca0fe7a8d3762345ec76674&redirect_uri=http://127.0.0.1:8000/guarantors&grant_type=refresh_token')
        return getrefreshresponse.json()
    except Exception as exception:
        context = {
            'exception': "Request Not found",
        }
        return HttpResponse(exception)

def getrefreshtoken():
    try:
        getrefreshresponse = requests.post('https://accounts.zoho.com/oauth/v2/token?refresh_token=1000.66fa270f2209b968a21f837ad243e0bd.41db074f2b1e3ab9b3f688bc056a2a5e&client_id=1000.61DFAE1NE31HICJJZC06O3EPY08W0V&client_secret=840dc61b265a5e413e2091d47c461a3af4324b314d&redirect_uri=https://guarantor.moove.africa/guarantors&grant_type=refresh_token')
        return getrefreshresponse.json()
    except Exception as exception:
        context = {
            'exception': "Request Not found",
        }
        return HttpResponse(exception)

def sendguarantordoc(request):
    # tokenjson = gettoken()
    refreshtokenjson = getrefreshtoken()
    Oauthtoken = tokenjson['access_token']
    file_list=[["FileName1","FilePath","application/pdf"],["FileName2","FilePath","application/pdf"]]
    respjson= createDocument(file_list,Oauthtoken)
    respjson=respjson['requests']
    request_id=respjson['request_id']
    submitrespjson=submitDocument(request_id,respjson,Oauthtoken)
    context = {
        'submitrespjson':submitrespjson
    }
    return render(request, 'guarantordoc/sentg.html', context)



def getDocumentDetailsById(request_id,Oauthtoken):
    headers = {'Authorization':'Zoho-oauthtoken '+Oauthtoken}
    r = requests.get('https://sign.zoho.com/api/v1/requests/'+request_id,headers=headers)
    return r.json()

def getDocumentStatus(request_id,Oauthtoken):
    response = getDocumentDetailsById(request_id,Oauthtoken)
    if response['status'] == 'success':
        status = response['requests']['request_status']
        if status == 'completed':
            print('Document signed by all parties')
        elif status == 'inprogress':
            actions = response['requests']['actions']
            print('Document in progress')
            for i in actions:
                if i['action_status'] == 'UNOPENED' or i['action_status'] == 'VIEWED':
                    print('Recipient yet to sign : '+i['recipient_email'])
    else:
        print('Error in get document : '+response['message'])

# Create your views here.
def search(request):

    try:
        guarantors = Guarantordetails.objects.get(id=request.user.id)
        
        # return HttpResponse(dl.to_dict('records'))
        return render(request, 'guarantordoc/search.html', guarantors)
    except requests.exceptions.ConnectionError:
        connection_status = "Connection refused"
        context = {
            'exception': connection_status,
        }
        return HttpResponse(requests.exceptions)
        messages.warning(request, connection_status)
        return HttpResponseRedirect('/search/index')
    except AssertionError as error:
        # Output expected AssertionErrors.
        # Logging.log_exception(error)
        context = {
            'exception': "Request Not found",
        }
       	return HttpResponse(error)
        messages.warning(request, 'Request Not found')
        return HttpResponseRedirect('/search/index')
    except Exception as exception:
        # Output unexpected Exceptions.
        # Logging.log_exception(exception, False)
        context = {
            'exception': "Request Not found",
        }
        return HttpResponse(exception)
        messages.warning(request, 'Request Not found')
        return HttpResponseRedirect('/search/index')


class OrderListJson(BaseDatatableView):
    # The model we're going to show
    model = Guarantordetails

    # define the columns that will be returned
    columns = ['guarantorid', 'firstname', 'lastname', 'email', 'phone']

    # define column names that will be used in sorting
    # order is important and should be same as order of columns
    # displayed by datatables. For non sortable columns use empty
    # value like ''
    order_columns = ['guarantorid', 'firstname', 'lastname', 'email', 'phone']

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 500

    def render_column(self, row, column):
        # We want to render user as a custom column
        if column == 'user':
            # escape HTML for security reasons
            return escape('{0} {1}'.format(row.firstname, row.lastname))
        else:
            return super(OrderListJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        # use parameters passed in GET request to filter queryset

        # simple example:
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(name__istartswith=search)

        # more advanced example using extra parameters
        filter_customer = self.request.GET.get('firstname', None)

        if filter_customer:
            customer_parts = filter_customer.split(' ')
            qs_params = None
            for part in customer_parts:
                q = Q(firstname__istartswith=part)|Q(lastname__istartswith=part)
                qs_params = qs_params | q if qs_params else q
            qs = qs.filter(qs_params)
        return qs