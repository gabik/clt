import os
import sys

sys.path.append('/home/gabi/clt')
os.environ['DJANGO_SETTINGS_MODULE'] = 'clt.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


