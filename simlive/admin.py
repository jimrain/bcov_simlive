from django.contrib import admin
from .models import BCAccount, Channel, Video, DayBlock, ProgramBlock

admin.site.register(BCAccount)
admin.site.register(Channel)
# Don't expose vidoe to the admin interface for now - might want to allow deletes later.
# BUT - leave it in for debugging. 
admin.site.register(Video)
admin.site.register(DayBlock)
admin.site.register(ProgramBlock)
