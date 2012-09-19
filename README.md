==============================================
app_account: user accounts for project template
==============================================

Provides user accounts to a project template.

INSTALL
============
1. Install Project Template

  django-admin.py startproject --template=https://github.com/zhouxb/project_template/zipball/master [project_name]

2. Install App Account

  pip install https://github.com/zhouxb/app_account/zipball/master

3. Add account to INSTALLED_APPS in settings.py

  INSTALLED_APPS = {
    ...
    account,
  }

4. Add account url in urls.py

  url(r'account/', include('account.urls')),

5. Create DB

  python manage.py schemamigration account --init
  python manage.py migrate account

