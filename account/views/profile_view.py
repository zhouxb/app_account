# -*- coding:utf8 -*-

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from annoying.decorators import render_to
from account.forms import UserEmailForm, UserProfileForm
from account.models import UserProfile

@render_to('account/profile/show.haml')
def update(request):
    userprofile, t = UserProfile.objects.get_or_create(user=request.user)
    if request.POST:

        useremail_form = UserEmailForm(request.POST, instance=request.user)
        userprofile_form = UserProfileForm(request.POST, instance=userprofile)

        if useremail_form.is_valid() and userprofile_form.is_valid():
            useremail_form.save()
            userprofile_form.save()
            return HttpResponseRedirect(reverse('profile_update'))
    else:
        useremail_form = UserEmailForm(instance=request.user)
        userprofile_form = UserProfileForm(instance=userprofile)

    return {
                'useremail_form':useremail_form,
                'userprofile_form':userprofile_form
            }

@render_to('account/profile/change_password.haml')
def change_password(request):
    if request.POST:
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile_update'))
    else:
        form = PasswordChangeForm(request.user)

    return {'form':form}

