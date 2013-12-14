from django.contrib import admin
from clt.models import xml_model, contact_group, group_members, contact_element, contact_phones

#class areaAdmin(admin.ModelAdmin):
        #list_display = ['id', 'parent', 'name']

admin.site.register(xml_model)
admin.site.register(contact_group)
admin.site.register(contact_phones)
admin.site.register(contact_element)
admin.site.register(group_members)

