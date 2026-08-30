import os
import sys

# 1. Point to virtual environment Python 3.9 interpreter
INTERP = "/home/sababeh1/virtualenv/sababehpar_website/3.9/bin/python"
if sys.executable != INTERP and os.path.exists(INTERP):
    os.execl(INTERP, INTERP, *sys.argv)

# 2. Add project directory and virtualenv site-packages to path
project_dir = os.path.dirname(os.path.abspath(__file__))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

site_packages = "/home/sababeh1/virtualenv/sababehpar_website/3.9/lib/python3.9/site-packages"
if site_packages not in sys.path and os.path.exists(site_packages):
    sys.path.insert(0, site_packages)


# 3. Set Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

# 4. Import WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

