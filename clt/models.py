from django.db import models
from django.contrib.auth.models import User

class xml_model(models.Model):
	user = models.ForeignKey(User, unique=False)
	xml_file = models.FileField(upload_to='tmp')

	def __unicode__(self):
		return str(self.user.username)

