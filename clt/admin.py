from django.contrib import admin
from clt.models import xml_model, contact_group

#class areaAdmin(admin.ModelAdmin):
        #list_display = ['id', 'parent', 'name']

admin.site.register(xml_model)
admin.site.register(contact_group)

