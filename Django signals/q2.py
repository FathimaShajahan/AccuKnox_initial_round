# Question 2: Do django signals run in the same thread as the caller?
#             Please support your answer with a code snippet that conclusively proves your stance.
#             The code does not need to be elegant and production ready, we just need to understand your logic.

# ANSWER:  Django signals run in the same thread as the caller.
#          This means that when a signal is sent, the signal handlers are
#          executed in the same thread as the code that triggered the signal.


import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=255)

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, created, **kwargs):
    print(f"Signal handler thread: {threading.get_ident()}")

# Create a new instance of MyModel
my_instance = MyModel(name="Test")
print(f"Main thread: {threading.get_ident()}")
my_instance.save()


# In this code  I use  threading.get_ident() function to get the identifier of the current thread.
# then  print the identifier in both the main thread (where the save() method is called) and in the signal handler.

# When I run this code, that the thread identifiers are the same for both the main thread
# and the signal handler. This demonstrates that the signal handler is executed in the same thread as the
# code that triggered the signal.