from django.contrib import admin
from models import Talk, Speaker

class TalkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Talk, TalkAdmin)
admin.site.register(Speaker)
