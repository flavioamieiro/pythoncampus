from django.contrib import admin
from models import Talk

class TalkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Talk)
