# QUESTION 1: By default are django signals executed synchronously or asynchronously?
# Please support your answer with a code snippet that conclusively proves your stance. 
# The code does not need to be elegant and production ready, we just need to understand your logic.

# ANSWER: By default django signals are synchronous because when a signal is sent,
#         the execution of the code that triggered the signal will be blocked until all the
#         signal handlers have finished executing.


import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=255)

@receiver(post_save, sender=MyModel)

def my_handler(sender, instance, created, **kwargs):
    print("Signal handler started")
    for i in range(5):
        print(f"Signal handler iteration {i+1}")
        time.sleep(1)  #  time taking task
    print("Signal handler finished")

    # Creating  a new instance of MyModel
my_instance = MyModel(name="Test")

print("Before save operation")

my_instance.save()
print("After save operation")


# In this code, the my_handler function runs five times, printing
# a message and pausing for one second during each iteration. This mimics
# a signal handler that takes time to complete.

# The message "After save operation" is printed only after the
# signal handler has finished running, which takes a total of five seconds.
# This shows that the signal is handled synchronously, meaning it blocks
# the execution of the code that triggered it.

# If the signal were handled asynchronously,
# the "After save operation" message would be printed immediately
# after calling the save() method, without waiting for the signal handler to finish