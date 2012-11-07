# coding:utf-8
from registration.backends.default import DefaultBackend
from accounts.forms import RegistrationForm


class BlankiBackend(DefaultBackend):

    def get_form_class(self, *args, **kwargs):
        return RegistrationForm
