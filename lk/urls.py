import slug as slug
from django.urls import path, re_path
from .views import *
from . import views

urlpatterns = [
	path('base/', base, name='base'),
	path('getTrump/', views.getTrump, name='getTrump'),
	path('getTehnika/', views.getTehnika, name='getTehnika'),
	path('ohrana_truda/', views.OhranaTruda.as_view(), name='ohrana_truda'),
	path('sotrudniki/', views.PersonList.as_view(), name='sotrudniki'),
	path('sotrudniki/filter', views.PersonalFilter.as_view(), name='filter'),
	path('sotrudniki/<slug:slug>/', views.CardUser.as_view(), name='card_user'),
	path('sotrudniki/<slug:slug>/update/', views.UserUpdate.as_view(), name='user_update'),
	path('', home, name='home'),
	path('login/', LoginUser.as_view(), name='login'),
	path('register/', RegPers.as_view(), name='register'),
	path('add_uch/', AddUch.as_view(), name='add_uch'),
	path('remonti/', views.RemontUcastki.as_view(), name='remonti'),
	path('remonti/<slug:slug>/', views.RemontDetail.as_view(), name='remont_detail'),
	path('upload_vtd', views.upload_vtd, name='upload_vtd'),

]
