from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Jobs
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def getJobs(request,page,size):
	if request.method == 'GET':
		skip = size * (page - 1)
		jobs = Jobs.objects.all()[skip:(page * size)]
		dict = {
			"jobs": list(jobs.values())
		}
		return JsonResponse(dict)
	else:
		return JsonResponse({"Status":"Error"})

@csrf_exempt
def deleteJobs(request,id):
	if request.method == 'DELETE' and Jobs.objects.filter(id=id).exists():
		job = Jobs.objects.get(id=id)
		job.delete()
		return JsonResponse({"Status":"Successfully deleted"})
	else:
		return JsonResponse({"Status":"Error"})

@csrf_exempt
def updateJobs(request,id):
	if request.method == 'PUT' and Jobs.objects.filter(id=id).exists() and request.body:
		decoded_data = request.body.decode('utf-8')
		data = json.loads(decoded_data)
		job = Jobs.objects.get(id=id)
		job.job_name = data['Title']
		job.job_details = data['Description']
		job.save()
		job = Jobs.objects.filter(pk=id)
		return JsonResponse({"job":list(job.values())})
	else:
		return JsonResponse({"Status":"Error","required":["Title","Description"]})

@csrf_exempt
def addJobs(request):
	if request.method == 'POST':
		try:
			decoded_data = request.body.decode('utf-8')
			data = json.loads(decoded_data)
			title = data['Title']
			des = data['Description']
			job = Jobs.objects.create(job_name =title , job_details=des)
			job = Jobs.objects.filter(id = job.pk)
			#successful
			return JsonResponse({"job":list(job.values())})
		except Exception as ex:
			print(ex)
			return JsonResponse({"Status":"Internal server error"})
	else:
		return JsonResponse({"Status":"Error","required":["Title","Description"]})
		