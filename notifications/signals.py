from django.db.models.signals import post_save
from django.dispatch import receiver
from tasks.models import Task, Comment
from .models import Notification

@receiver(post_save, sender=Task)
def create_task_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.assigned_to,
            content=f'You have been assigned to the task: {instance.title}',
            notification_type='TASK_ASSIGNED'
        )
    else:
        Notification.objects.create(
            user=instance.assigned_to,
            content=f'The task "{instance.title}" has been updated',
            notification_type='TASK_UPDATED'
        )
    
@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.task.assigned_to,
            content=f'A new comment has been added to the task: {instance.task.title}',
            notification_type='COMMENT_ADDED'
        )