from django.contrib.auth.models import User
from django.db import models

class KitherderUser(models.Model):
	kitherderuser_user = models.ForeignKey(User);
	
class Mentor(models.Model):
	mentor_user = models.ForeignKey(KitherderUser);	
	
class Mentee(models.Model):
	mentee_user = models.ForeignKey(KitherderUser);
	
class Project(models.Model):
	project_mentee = models.ForeignKey(Mentee,null=True);
	project_mentor = models.ForeignKey(Mentor,null=True);
	project_short_description = models.CharField(max_length=200);