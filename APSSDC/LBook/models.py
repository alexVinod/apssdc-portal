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
	
class DistrictOfficer(models.Model):
	district_choices = (('srikakulam','Srikakulam'),
				 ('vizinagaram','Vizinagaram'),
				 ('visakapatnam','Visakapatnam'),
				 ('eastGodavari','East Godavari'),
				 ('krishna','Krishna'),
				 ('westGodavari','West Godavari'),
				 ('guntur','Guntur'),('prakasam','Prakasam'),
				 ('nellore','Nellore'),
				 ('chittoor','Chittoor'),('kadapa','Kadapa'),
				 ('ananthapur','Ananthapur'),('kurnool','Kurnool'))
	district=models.CharField(max_length=300,choices=district_choices)
	name=models.CharField(max_length=600)
	contact = models.CharField(max_length=20)
	email = models.CharField(max_length=100)

	def __str__(self):
		return self.district+" -- "+self.name

class Gallery(models.Model):
	hideShow_choices = (('hide','Hide'),('show','Show'))

	eventName = models.CharField(max_length=600)
	image = models.ImageField(upload_to='static/images/gallery/')
	description = models.CharField(max_length=1000)
	hide_show = models.CharField(max_length=50,choices=hideShow_choices)
	def __str__(self):
		return self.eventName+" -- "+self.image.url+" -- "+self.hide_show