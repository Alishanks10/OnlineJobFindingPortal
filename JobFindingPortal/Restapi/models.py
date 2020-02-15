from django.db import models

# Create your models here.

class Jobs(models.Model):
	job_name = models.CharField(max_length=30)
	job_details = models.TextField()

	def __str__(self):
		return str(job_name)+str(job_details) 