from django.db import models
from django.conf import settings
from django.urls import reverse

# pip install misaka
import misaka

from forums.models import Forum

from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    content_html = models.TextField(editable=False)
    forum = models.ForeignKey(Forum, related_name="posts",null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        self.content_html = misaka.html(self.content)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "posts:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user", "content"]
