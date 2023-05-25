from django.db.models import *

class Project(Model):
	project_title = CharField('Title', max_length=512, unique=True)
	project_img = ImageField('Image', upload_to='projects/')
	project_body = TextField('Description')

	project_time = IntegerField('Time', default=0)
	project_price = FloatField('Time', default=0)

	project_date = DateTimeField('Date and Time', auto_now_add=True)

	def __str__(self):
		return self.project_title

	class Meta:
		verbose_name = 'Project'
		verbose_name_plural = 'Projects'