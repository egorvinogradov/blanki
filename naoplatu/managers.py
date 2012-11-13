# coding:utf-8
from django.db import models


class InvoiceManager(models.Manager):

    def get_query_set(self, *args, **kwargs):
        return super(InvoiceManager, self).get_query_set(*args, **kwargs).filter(is_deleted=False)
