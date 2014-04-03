# -*- coding: utf-8 -*-
from cms.extensions import PageExtension, TitleExtension
from cms.extensions.extension_pool import  extension_pool
from django.contrib.auth.models import User
from django.db import models

class MyPageExtension(PageExtension):
    extra = models.CharField(blank=True, default='', max_length=255)
    favorite_users = models.ManyToManyField(User, blank=True, null=True)

    def copy_relations(self, other, language):
        for favorite_user in other.favorite_users.all():
            favorite_user.pk = None
            favorite_user.mypageextension = self
            favorite_user.save()

extension_pool.register(MyPageExtension)


class MyTitleExtension(TitleExtension):
    extra_title = models.CharField(blank=True, default='', max_length=255)

extension_pool.register(MyTitleExtension)
