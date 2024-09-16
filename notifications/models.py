from django.db import models
from django.conf import settings

# Create your models here.

class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ('TASK_ASSIGNED', 'Task Assigned'),
        ('TASK_UPDATED', 'Task Updated'),
        ('COMMENT_ADDED', 'Comment Added'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    content = models.TextField()
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.get_notification_type_display()} for {self.user.username}"