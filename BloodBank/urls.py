from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.home, name="home"),
    path("home",views.home, name="homee"),
    path("donateblood",views.donate, name="donateblood"),
    path("requestblood",views.addbloodrequest, name="requestblood"),

    path("bloodbasics",views.bloodbasics, name="bloodbasics"),
    path("bloodbankinfo",views.bloodbankinfo, name="bloodbankinfo"), 

    path('event', views.event, name="event"),
    path("addEventForm",views.addEventForm, name="addeventform"),
    path("getEventForm", views.getEventForm, name="geteventform"),
    path('updateEventForm/<int:event_id>', views.updateEventForm, name="updateeventform"),

    path('addTeamForm', views.addTeamForm, name="addteamform"),
    path('getTeamForm', views.getTeamForm, name="getteamform"),
    path('updateTeamForm/<int:team_id>', views.updateTeamForm, name="updateteamform"),
    path('deleteTeamForm/<int:team_id>', views.deleteTeamForm, name="deleteteamform"),

    path('contactform', views.contact_form, name="contactform"),
    path('covid', views.covid, name="covid"),

]

