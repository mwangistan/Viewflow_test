from django.db import models
from viewflow.models import Process

#Stores flow state of the process (process instance and associated tasks)
class HelloWorldProcess(Process):
	text = models.CharField(max_length=150)
	approved = models.BooleanField(default=False)
