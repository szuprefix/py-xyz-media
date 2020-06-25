# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals

STATUS_PROCESS = 1
STATUS_DONE = 2
STATUS_FAIL = 0

STATUS = (
    (STATUS_PROCESS, '转码中'),
    (STATUS_DONE, '完成'),
    (STATUS_FAIL, '失败')
)
