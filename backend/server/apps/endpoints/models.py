from django.db import models

# Create your models here.
class Endpoint(models.Model):
	'''
	The endpoint object represents ML API endpoint.

	Attributes:
		name : name of API, it will be used in URL
		owner: owner name string
		created_at: date of creation of end point.

	'''

	name = models.CharField(max_length = 128)
	owner = models.CharField(max_length = 128)
	created_at = models.DateTimeField(auto_now_add=True, blank = True)

class MLAlgo(models.Model):
	