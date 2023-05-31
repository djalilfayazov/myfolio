from django.shortcuts import render
from .models import *


def index(request):
	return render(
		request, 'index.html', {
			'project_count': Project.objects.count(),
			'projects': Project.objects.all(),

			'certs': Certificate.objects.all()
		}
	)