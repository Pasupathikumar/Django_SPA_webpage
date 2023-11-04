from django.contrib import admin
from .models import ProjectDetails
# Register your models here.
#register the DB
class Project_data(admin.ModelAdmin):
    project_details=['project_title', 'company_name', 'person_name', 'email_id', 'phone_number', 'project_summary', 'project_planning', 'tools_or_others', 'tools_version', 'price']
    pass
admin.site.register(ProjectDetails, Project_data)



