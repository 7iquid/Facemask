from django.contrib import admin
# Register your models here.
from .models import Machine,McDailyRecordingArea,McRecordingArea
# from .models import Note

admin.site.register((Machine,McDailyRecordingArea,McRecordingArea))