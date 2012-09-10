from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import ugettext, ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

def validate_even(value):
    if value != '2':
        raise ValidationError(u'here')

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(_('phone'), max_length=50, null=True, blank=True,
            validators=[RegexValidator(regex='^(1?(-?\d{3})-?)?(\d{3})(-?\d{4})$',
                message=_('phone format error'))])

    class Meta:
        app_label = 'account'

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

