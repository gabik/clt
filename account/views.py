# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
#from account.forms import 
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.utils import simplejson as json
from account.models import status, UserProfile
from account.forms import  UserForm
from django.core import serializers
from django.core.mail import EmailMultiAlternatives
import hashlib

def Plogin (request):
	json_data=list(status.objects.filter(status='ERR',MSG='NE'))
	if request.method == 'POST':
		json_data=list(status.objects.filter(status='ERR',MSG='NE'))
		new_user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if new_user :
			json_data = status.objects.filter(status='OK')
			if new_user.is_active:
				login(request, new_user)
			else:
				json_data=list(status.objects.filter(status='ERR',MSG='PD'))
	json_dump = serializers.serialize("json", json_data)
	return HttpResponse(json_dump)

def PNewUser(request):
	json_data=status.objects.filter(status='ERR',MSG='PD')
	errors=""
	if request.method == 'POST':
		#userprofile_form = UserProfileForm(request.POST)
		user_form = UserForm(request.POST)
		#if userprofile_form.is_valid() and user_form.is_valid():
		if user_form.is_valid():
			user_clean_data = user_form.cleaned_data
			created_user = User.objects.create_user(user_clean_data['username'], user_clean_data['email'], user_clean_data['password1'])
			created_user.first_name=request.POST['firstname']
			created_user.last_name=request.POST['lastname']
			created_user.is_active = False
			created_user.save()
			userprofile = UserProfile(user=created_user, hash=hashlib.sha224("CLT" + created_user.username + created_user.email).hexdigest())
			#userprofile.user = created_user
			#userprofile.phone_num1 = userprofile_form.cleaned_data['phone_num1']
			#userprofile.hash = hashlib.sha224("CLT" + created_user.username + created_user.email).hexdigest()
			userprofile.save()
			subject = "new provider notice"
			accept_link = 'http://cl.kazav.net/account/validate_prov/' + str(created_user.id) + '/' + userprofile.hash + '/'
			html_message = '<meta http-equiv="Content-Type" content="text/html; charset=utf-8">Welcome to CLT<BR> Name: ' + created_user.first_name + ' ' + created_user.last_name + '<BR> <a href="' + accept_link + '"> Validate Me </a> '
			text_message = 'Welcome to CLT. Name: ' + created_user.first_name + ' ' + created_user.last_name + '      Validate yourself at: ' + accept_link 
			user_mail=created_user.email
			msg = EmailMultiAlternatives(subject, text_message, 'CLT Server<contact@clt.com>', [user_mail])
			msg.attach_alternative(html_message,"text/html")
			msg.send()
			#new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
			#login(request, new_user)
			json_data = status.objects.filter(status='OK')
		else:
			json_data = status.objects.filter(status='WRN')
			if user_form.errors.items() :
				errors = ",[" + str(dict([(k, v[0].__str__()) for k, v in user_form.errors.items()])) + "]"
			#if userprofile_form.errors.items():
			#	errors += ",[" + str(dict([(k, v[0].__str__()) for k, v in userprofile_form.errors.items()])) + "]"
	json_dump = "[" + serializers.serialize("json", json_data)
	json_dump += errors + "]"
	return HttpResponse(json_dump.replace('\'','"'))
