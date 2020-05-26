# PythonAnywhere Flask app setup
REFERENCE: https://help.pythonanywhere.com/pages/Flask/

From root folder, first setup virtualenv:
```
mkvirtualenv --python=/usr/bin/python3.8 my-virtualenv  # NOTE: We are using python version same as the list in Web tab.
pip install flask
```

Then cd to flaskapp folder and execute
```
pip install -r requirements.txt
```

Goto Web tab, eg. https://www.pythonanywhere.com/user/<yourusername>/webapps/

and in 'VirtualEnv' section type name of your virtualenv, save and then tap on reload button on top.

In 'Code' section on Web tab, edit 'https://www.pythonanywhere.com/user/<yourusername>/files/var/www/<yourusername>_pythonanywhere_com_wsgi.py?edit'

- Update line:
project_home = '/home/<yourusername>/<changethistoyourfolder>'
- Update line
from <changetomainfilename> import app as application  # noqa


save and then reload application.

Web app should now be accessible at http://<yourusername>.pythonanywhere.com/