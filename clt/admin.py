from django.contrib import admin
from clt.models import xml_model

#class areaAdmin(admin.ModelAdmin):
        #list_display = ['id', 'parent', 'name']

admin.site.register(xml_model)

