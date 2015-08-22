from django.db import models

class Housemate(Models.model):
	name=models.CharField(max_length=100)
	phone_number=models.CharField(max_length=10) # Format should be ##########
	email=models.EmailField()

class Bill(Models.model):
	title=models.CharField(max_length=200)
	cost=models.Double