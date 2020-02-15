from django.db import models

# Create your models here.
class Job(models.Model):
	title = models.CharField(max_length=100)
	details = models.CharField(max_length=500)
	date_posted = models.CharField(max_length=100)
	job_description = models.FileField(upload_to='Job_Description')
	def __str__(self):
		# return self.title
		return 'title : {0} date_posted: {1}'.format(self.title, self.date_posted)