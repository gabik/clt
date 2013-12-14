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
		return str(self.user.username + ' -> ' + self.group.name + '(' + str(self.group.id) + ')') 

class contact_element(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=254)
	group = models.ForeignKey(contact_group, unique=False)

	def __unicode__(self):
		return str(self.name + '(' + str(self.id) + ')' + ' -> ' + self.group.name + '(' + str(self.group.id) + ')')

class contact_phones(models.Model):
	contact = models.ForeignKey(contact_element, unique=False)
	phone = models.IntegerField(max_length=13) # unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])
	type = models.CharField(max_length=50)

	def __unicode__(self):
		return str(self.contact.name + '(' + str(self.contact.id) + ')' + ' - ' + str(self.phone) + ' (' + self.type + ') ')
