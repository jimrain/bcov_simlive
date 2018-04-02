from django.contrib import admin
from .models import BCAccount, Channel, Video, DayBlock, ProgramBlock

admin.site.register(BCAccount)
admin.site.register(Channel)
admin.site.register(Video)
admin.site.register(DayBlock)
admin.site.register(ProgramBlock)
