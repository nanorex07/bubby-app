from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
import uuid
from mimetypes import guess_type


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts")
    media = models.FileField(upload_to="post_files", blank=False)
    caption = models.TextField(blank=True, max_length=120)
    created_at = models.DateField(default=datetime.now)
    likes = models.ManyToManyField(User)

    def media_type_html(self):
        type_tuple = guess_type(self.media.url, strict=True)
        if (type_tuple[0]).__contains__("image"):
            return "image"
        elif (type_tuple[0]).__contains__("video"):
            return "video"

    def __str__(self):
        return self.user.username + "_post"


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.author.username+"_comment_on_"+self.post.user.username+"_post"
