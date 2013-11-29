from django import forms
from clt.models import xml_model
from django.forms import ModelForm
import csv

class xml_form(ModelForm):
	class Meta:
		model = xml_model
		fields = ("xml_file",)
