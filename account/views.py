# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
#from account.forms import 
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.utils import simplejson as json
from account.models import status
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
