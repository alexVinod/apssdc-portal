from django.urls import path
from . import views
app_name="lbook"
urlpatterns=[
	path("",views.home,name="home"),
	# path("home",views.home1,name="homes"),
# 			    Home
# About Us 
# DashBoard 
# Skill Stories 
# Institute Finder 
# Tenders 
# Jobs
# Skill Development
# Careers
# Media 
# Contact
	path("Clientbook",views.comingSoon,name="cs"),
	path("about-us",views.aboutUs,name="about"),
	path("board-directors",views.boardDirectors,name="board"),
	path("dash-board",views.comingSoon,name="dashboard"),
	path("skillstories",views.comingSoon,name="skillstories"),
	path("institues",views.comingSoon,name="institues"),
	path("tenders",views.comingSoon,name="tenders"),
	path("jobs",views.comingSoon,name="jobs"),
	path("sdc",views.comingSoon,name="sdc"),
	path("careers",views.comingSoon,name="careers"),
	path("media",views.comingSoon,name="media"),
	path("contact",views.comingSoon,name="contact"),
]