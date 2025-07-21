# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Drivers(models.Model):

    #__Drivers_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    class_name = models.CharField(max_length=255, null=True, blank=True)
    id = models.IntegerField(null=True, blank=True)

    #__Drivers_FIELDS__END

    class Meta:
        verbose_name        = _("Drivers")
        verbose_name_plural = _("Drivers")


class Device Profiles(models.Model):

    #__Device Profiles_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    driver = models.ForeignKey(Drivers, on_delete=models.CASCADE)
    cred_username = models.CharField(max_length=255, null=True, blank=True)
    cred_password = models.CharField(max_length=255, null=True, blank=True)
    snmp_enabled = models.BooleanField()
    snmp_version = models.CharField(max_length=255, null=True, blank=True)
    backup_profile = models.ForeignKey(Backup Profiles, on_delete=models.CASCADE)

    #__Device Profiles_FIELDS__END

    class Meta:
        verbose_name        = _("Device Profiles")
        verbose_name_plural = _("Device Profiles")


class Backup Profiles(models.Model):

    #__Backup Profiles_FIELDS__
    cronjob = models.CharField(max_length=255, null=True, blank=True)
    retention = models.IntegerField(null=True, blank=True)

    #__Backup Profiles_FIELDS__END

    class Meta:
        verbose_name        = _("Backup Profiles")
        verbose_name_plural = _("Backup Profiles")



#__MODELS__END
