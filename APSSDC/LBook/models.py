from django.db import models


class Job(models.Model):
	s_choices = (('active','Active'),('inactive','InActive'))
	date = models.DateField()
	place = models.CharField(max_length=30)
	link = models.CharField(max_length=500,default="#")
	desc = models.CharField(max_length=500)
	status = models.CharField(max_length=9,choices=s_choices)

	def __str__(self):
		return str(self.date)+"-"+str(self.place)
	"""docstring for jobs
"""
class Update(models.Model):
	s_choices = (('active','Active'),('inactive','InActive'))
	date = models.DateField()
	place = models.CharField(max_length=30)
	link = models.CharField(max_length=500,default="#")
	desc = models.CharField(max_length=500)
	status = models.CharField(max_length=9,choices=s_choices)
	
	def __str__(self):
		return str(self.date)+"-"+str(self.place)

class Acheivement(models.Model):
	registered = models.CharField(max_length=30)
	skilledYouth = models.CharField(max_length=30)
	tPs = models.CharField(max_length=30)
	employers = models.CharField(max_length=30)
	institutes = models.CharField(max_length=30)
	collaborations = models.CharField(max_length=30)

	def __str__(self):
		return str("TOTAL ACHEIVEMENTS")

class Director(models.Model):
	image = models.ImageField(upload_to='static/images/board/')
	name = models.CharField(max_length=30)
	depts = models.CharField(max_length=250,blank=True,null=True)
	desig_apssdc = models.CharField(max_length=30)

	def __str__(self):
		return self.name
	

