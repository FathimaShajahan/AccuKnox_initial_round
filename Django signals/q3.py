# QUESTION 3: By default do django signals run in the same database transaction as the caller? 
#             Please support your answer with a code snippet that conclusively proves
#             your stance. The code does not need to be elegant and production ready,
#             we just need to understand your logic.


# ANSWER : Yes, Django signals run in the same database transaction as the caller by default. 
#          This means that if an exception is raised in a signal handler, it will roll back 
#          the entire transaction, including the original operation that triggered the signal.

#          This is because Django 's signal system is designed to work within the context of a
#          database transaction. When a signal is sent, the signal handlers are executed within the same
#          transaction as the code that triggered the signal.

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=255)

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, created, **kwargs):
    raise Exception("Something went wrong")

try:
    my_instance = MyModel(name="Test")
    my_instance.save()
    print("Instance was saved")
except Exception as e:
    print(f"Exception caught: {e}")

try:
    MyModel.objects.get(name="Test")
    print("Instance was saved")
except MyModel.DoesNotExist:
    print("Instance was not saved")
    
    
#In this code, I define a signal handler my_handler that raises an exception
# when the post_save signal is triggered.Then it create a new instance of MyModel
# and try to save it. If the instance is saved, it can print "Instance was saved".
# If an exception is caught, it can print the exception message.

