from django.shortcuts import render
from .models import *
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse,JsonResponse
from pathlib import Path
import os
import datetime
# Create your views here.
company=CompanyInformation.objects.all()
def index(request):

    contex={
        'company': company,
    }
    return render(request,'index.html',contex)


def reportV(request):
    recive=CashReceiveList.objects.all();
    expence=ExpenseList.objects.all();
    return render(request, 'Report.html',{'recive':recive,'expence':expence})




def All_ReceivedV(request):
    from_dates=request.POST.get('fdate')
    fdatea = datetime.datetime.strptime(from_dates, '%Y-%m-%d')
    to_dates=request.POST.get('tdate')
    todates = datetime.datetime.strptime(to_dates, '%Y-%m-%d')
    arecived = CashReceiveEntry.objects.filter(To_Date__range=(fdatea,todates))
    total=CashReceiveEntry.objects.raw('SELECT id=0 as id, sum(amount) as Amount from personal_cashreceiveentry where To_Date BETWEEN %s and %s',[fdatea,todates])
    template_path = 'report/AllReceived.html'
    BASE_DIR = Path(__file__).resolve().parent.parent
    path = os.path.join(BASE_DIR, 'project\static')
    context = {'company': company, 'path': path,'arecived':arecived,'total':total}
    response = HttpResponse(content_type='application/pdf')
    # for downlode
    # response['Content-Disposition'] = 'attachment; filename="reports.pdf"'
    response['Content-Disposition'] = 'filename="reports.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def All_ExpenseV(request):
    from_dates = str(request.POST.get('fdate'))
    fdatea = datetime.datetime.strptime(from_dates, '%Y-%m-%d')
    to_dates = request.POST.get('tdate')
    todates = datetime.datetime.strptime(to_dates, '%Y-%m-%d')
    arecived = ExpenseEntry.objects.filter(To_Date__range=(fdatea,todates))
    total=CashReceiveEntry.objects.raw('SELECT id=0 as id, sum(amount) as Amount from personal_expenseentry where To_Date BETWEEN %s and %s',[fdatea,todates])
    template_path = 'report/AllExpense.html'
    BASE_DIR = Path(__file__).resolve().parent.parent
    path = os.path.join(BASE_DIR, 'project\static')
    context = {'company': company, 'path': path, 'arecived': arecived,'total':total}
    response = HttpResponse(content_type='application/pdf')
    # for downlode
    # response['Content-Disposition'] = 'attachment; filename="reports.pdf"'
    response['Content-Disposition'] = 'filename="reports.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
