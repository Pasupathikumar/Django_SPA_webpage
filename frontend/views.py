from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Project_details_form
from .models import ProjectDetails
from django.urls import reverse

from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse

from django.contrib import messages
form_data={}
def main_page(request):
    obj = ProjectDetails.objects.all()
    return render(request, 'main_page.html', {'obj': obj})
def add_project(request):

    if request.method == 'POST':


        ProjectDetails(
            project_title=request.POST['project_title'],
            company_name=request.POST['company_name'],
            person_name=request.POST['person_name'],
            email_id=request.POST['email_id'],
            phone_number=request.POST['phone_number'],
            project_summary=request.POST['project_summary'],
            project_planning=request.POST['project_planning'],

            tools_or_others=request.POST['input1_1'],

            tools_version=request.POST['input1_2'],
            price=request.POST['input1_3']


        ).save()

        return redirect('main_page')

        #messages.success(request, "Datas are recorded successfully")

    return HttpResponse("Invalid form data")

def edit_content(request, record_id):
    record = get_object_or_404(ProjectDetails, id=record_id)

    if request.method == 'POST':
        record.project_title = request.POST.get('project_title')
        record.company_name = request.POST.get('company_name')
        record.person_name = request.POST.get('person_name')
        record.email_id = request.POST.get('email_id')
        record.phone_number = request.POST.get('phone_number')
        record.project_planning = request.POST.get('project_planning')
        record.project_summary = request.POST.get('project_summary')
        record.tools_or_others = request.POST.get('tools_or_others')
        record.tools_version = request.POST.get('tools_version')
        record.price = request.POST.get('price')
        record.save()
        return HttpResponseRedirect(reverse('main_page'))

    return render(request, 'main_page.html', {'record': record})
def delete_content(request, pk):
    project = ProjectDetails.objects.get(id=pk)
    project.delete()
    return HttpResponse('Details deleted..')

def recreate_content(request, pk):
    project=ProjectDetails.objects.get(id=pk)

    new_project=ProjectDetails(
                               project_title=project.project_title,
                               company_name=project.company_name,
                               person_name=project.person_name,
                               email_id=project.email_id,
                               phone_number=project.phone_number,
                               project_summary=project.project_summary,
                               project_planning=project.project_planning,
                               tools_or_others=project.tools_or_others,
                               tools_version=project.tools_version,
                               price=project.price
                               )
    new_project.save()
    return HttpResponse('order recreated successfully')