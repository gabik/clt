import datetime
from django.db.models import Max
#from clt.models import 
#from clt.forms import 
#from account.models import 
from django.utils import simplejson as json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.core import serializers
from clt import settings
from account.models import status
from clt.forms import xml_form
import xml.etree.ElementTree as ET

def create_new_group(request):
	xml1=request.POST
	return HttpResponse(xml1)

def handle_uploaded_file(file_path, user_id):
	dest = open(settings.MEDIA_ROOT + "/contacts_xml/" + str(user_id),"wb")
	for chunk in file_path.chunks():
		dest.write(chunk)
	dest.close()

@login_required(login_url='/account/logout/', redirect_field_name=None)
def post_xml(request):
	json_data=list(status.objects.filter(status='ERR',MSG='NE'))
	errors=""
	if request.method == 'POST':
		new_xml = xml_form(request.POST, request.FILES)
		if new_xml.is_valid():
      #work_pic = work.objects.filter(id=request.POST['work_id'])
      #if work_pic:
      #  user_work = work_pic[0].client_user
      #  if user_work == request.user:
			handle_uploaded_file(request.FILES["xml_file"], request.user.id)
			#xml_clean = new_xml.cleaned_data
			cur_xml = new_xml.save(commit=False)
			cur_xml.user = request.user
			cur_xml.xml_file = "contacts_xml/" + str(request.user.id)
			cur_xml.save()
			json_data = status.objects.filter(status='OK')
      #  else:
      #    json_data=list(status.objects.filter(status='ERR',MSG='PD'))
		else:
			json_data = status.objects.filter(status='WRN',MSG="")
      #errors = list(pic_form.errors.items())
			errors = str([(k, v[0].__str__()) for k, v in new_xml.errors.items()])
  #else:
    #pic_form = new_pic()
    #return render_to_response('oos/post_pic.html', { 'pic_form': pic_form}, context_instance=RequestContext(request))
	json_dump = serializers.serialize("json", json_data)
	json_dump += errors
	return HttpResponse(json_dump)


# XML PARSE:
# path = "/home/gabi/clt/static/1.xml"
# tree = ET.parse(path)
# root=tree.getroot()
# ## Adding the group and getting its ID key
# gname=root.find("Group").find("Name").text
# gowner=root.find("Group").find("Owner").text
# ## Adding contacts to the group
# for i in root.find("Contacts"):
 # i.find("Name").text
 # i.find("Email").text
 # ## save it
 # ## adding phones to phones list
 # for j in i.find("Phones"):
  # j.find("Number").text
  # j.find("Type").text
  # ## save the phone on the model with the contact key

