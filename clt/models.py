from django.db import models
from django.contrib.auth.models import User

class xml_model(models.Model):
	user = models.ForeignKey(User, unique=False)
	xml_file = models.FileField(upload_to='tmp')

	def __unicode__(self):
		return str(self.user.username)

class contact_group(models.Model):
	name = models.CharField(max_length=50)
	owner = models.ForeignKey(User, unique=False)

	def __unicode__(self):
		return str(self.name)

class group_members(models.Model):
	user = models.ForeignKey(User, unique=False)
	group = models.ForeignKey(contact_group, unique=False)

	def __unicode__(self):
		return str(self.user.username + ' -> ' + self.group.name + '(' + self.group.id + ')') 
