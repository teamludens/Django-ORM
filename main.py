############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys

sys.dont_write_bytecode = True

# Django specific settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
import django

django.setup()

# Import your models for use in your script
from db.models import *

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """
from push_notifications.gcm import send_message

# https://github.com/jazzband/django-push-notifications/blob/13a2c6f7b34ab884f65e2791841549975795bebf/push_notifications/models.py#L104
registration_id = "evOTBcDgJ0wKtrjrxuFiXr:APA91bFzEFMhIQTWpwmB_GlGZ9FKMZhYA77sCJohGvGw4NCBkJE3rn-SbpzGCSQ-IZ3Unct_DLHrsm-pdcnvXq-zTDW5ZEE1FAngdkAm2099hTK0rzDhu_inJTGi-nyLVYaSz9wCZ-uz"
data = {"target": "와인모임이 개설되었습니다.", "description": "dfasdf", "message": "test"}
badge = 1

send_message(registration_id, data, "FCM", application_id=None, badge=badge)
