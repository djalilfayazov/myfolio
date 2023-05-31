from django.shortcuts import render
from .models import *

from datetime import datetime as dt
from datetime import date

def index(request):
	return render(
		request, 'index.html', {
			'project_count': Project.objects.count(),
			'projects': Project.objects.all(),

			'certs': Certificate.objects.all(),

			# --------------------

			'exp': (dt.now()  - dt(2021, 9, 22)).days
		}
	)