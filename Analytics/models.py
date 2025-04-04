from django.conf import settings  # Import settings
from django.db import models

class UserVisit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use AUTH_USER_MODEL
    visit_time = models.DateTimeField(auto_now_add=True)
    page_visited = models.CharField(max_length=200)
    ip_address = models.GenericIPAddressField()


    def __str__(self):
        return f"Visit by {self.user.username} to {self.page_visited} at {self.visit_time}"
