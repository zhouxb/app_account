# -*- coding:utf8 -*-

from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from annoying.decorators import render_to, ajax_request
import django_tables2 as tables
from django_tables2 import Attrs
from account.forms import UserForm, UserProfileForm
from account.models import UserProfile

class AccountTable(tables.Table):
    check = tables.CheckBoxColumn(attrs=Attrs(th={'width':50}))
    username = tables.Column()
    email = tables.Column(verbose_name='mail')
    operating = tables.TemplateColumn(template_name='account/operate.haml')

    class Meta:
        attrs = {'class': 'table table-bordered'}
        orderable = False

@permission_required('auth.change_user')
@render_to('account/index.haml')
def index(request):
    object_list = User.objects.all()
    queryset = User.objects.all()
    table = AccountTable(queryset)
    return {'table':table}

@render_to('account/new.haml')
def create(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('account_index'))
    else:
        form = UserCreationForm()

    return {'form':form}

@render_to('account/show.haml')
def update(request, id):
    user = User.objects.get(id=id)

    if request.POST:
        user_form = UserForm(request.POST, instance=user)
        setpassword_form = SetPasswordForm(user, request.POST)

        new_password1 = request.POST.get('new_password1', '')
        new_password2 = request.POST.get('new_password2', '')

        if not new_password1 and not new_password2:
            if user_form.is_valid():
                user_form.save()
                return HttpResponseRedirect(reverse('account_index'))

        else:
            if user_form.is_valid() and setpassword_form.is_valid():
                user_form.save()
                setpassword_form.save()
                return HttpResponseRedirect(reverse('account_index'))

    else:
        user_form = UserForm(instance=user)
        setpassword_form = SetPasswordForm(user)

    return {
                'user_form':user_form,
                'setpassword_form':setpassword_form,
                'id':id
            }

@ajax_request
def delete(request, id):
    response = {}
    response['result'] = 'success'
    try:
        User.objects.get(id=id).delete()
    except:
        response['result'] = 'failure'
    return response

