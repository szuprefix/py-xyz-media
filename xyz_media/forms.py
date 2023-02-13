# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals
from django.forms import Form, FileField

class FileUploadForm(Form):
    file = FileField()