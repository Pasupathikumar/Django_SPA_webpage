from django import forms
from .models import ProjectDetails

class Project_details_form(forms.ModelForm):
    class Meta:
        model=ProjectDetails
        fields=['project_title', 'company_name', 'person_name', 'email_id', 'phone_number', 'project_summary', 'project_planning','tools_or_others', 'tools_version', 'price']
