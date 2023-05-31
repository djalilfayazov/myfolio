from django.contrib.admin import *
from .models import *


@register(Project)
class ProjectAdmin(ModelAdmin):
	list_display = ('id', 'project_title', 'project_date')
	list_display = ('id', 'project_title')
	ordering = ('id',)


@register(Certificate)
class CertificateAdmin(ModelAdmin):
	list_display = ('id', 'title')
	list_display_links = ('id', 'title')
	ordering = ('id',)