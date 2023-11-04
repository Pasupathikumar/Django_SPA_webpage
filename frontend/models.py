from django.db import models

# Create your models here.

class ProjectDetails(models.Model):
    project_title = models.CharField(max_length=2500, null=False)
    company_name = models.CharField(max_length=2500, null=False)
    person_name = models.CharField(max_length=250,  null=False)
    email_id = models.EmailField( null=False)
    phone_number = models.CharField(max_length=20,  null=False)
    project_summary = models.TextField( null=False)
    project_planning = models.TextField( null=False)

    tools_or_others=models.TextField()
    tools_version=models.TextField()
    price=models.TextField()

        #return self.project_title, self.company_name, self.person_name, self.email_id, self.phone_number, self.project_summary, self.project_planning

