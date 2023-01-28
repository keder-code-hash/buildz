from django.db import models

COMMERCIAL = 'CL'
INDUSTRIAL = 'IL'
RESIDENTIAL = 'RL' 
PROJECT_TYPE = [
    (COMMERCIAL, 'Commercial'),
    (INDUSTRIAL, 'Industrial'),
    (RESIDENTIAL, 'Residential')
]
timeline1='ASAP'
timeline2='Within the next Week/Few Weeks'
timeline3='Within the next Month/Few Months'
PROJECT_TIMELINE = [
    (timeline1,'ASAP'),
    (timeline2,'Within the next Week/Few Weeks'),
    (timeline3,'Within the next Month/Few Months')
]
ONGOING = 'ong'
COMPLETED = 'compl'
PROJECT_STATUS = [
    (ONGOING,'Ongoing'),
    (COMPLETED,'Completed')
]

# status bar system should be implemeneted too related to a project.

class Project(models.Model):
    name = models.CharField(max_length=255,blank=False,null=False)
    address = models.CharField(max_length=255,blank=False,null=False)
    city = models.CharField(max_length=255,blank=False,null=False)
    postal_code = models.CharField(max_length=30,blank=False,null=False)
    type = models.CharField(
        max_length=2,
        choices=PROJECT_TYPE,
        default=COMMERCIAL,
    )
    description = models.CharField(max_length=255,blank=True,null=True)
    timeline = models.CharField(
        max_length=80,
        choices=PROJECT_TIMELINE,
        default=timeline1
    )
    # If project status is ongoing then user does not provide all data for it and it will 
    # in the ongoing pannel. If status is completed then it will shift to the proposal pannel.
    status = models.CharField(
        max_length=10,
        choices=PROJECT_STATUS,
        default=ONGOING
    )
    

    created_at = models.DateTimeField(auto_created=True,auto_now_add=True)
    updated_at = models.DateTimeField(auto_created=True,auto_now=True)
