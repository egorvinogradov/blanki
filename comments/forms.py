#coding:utf-8
from django import forms
from django.contrib.comments import forms as comment_forms


class CommentForm(comment_forms.CommentForm):

    email = forms.EmailField(
        widget=forms.HiddenInput, required=False, max_length=255
    )
    url = forms.URLField(
        widget=forms.HiddenInput, required=False, max_length=255
    )
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)
