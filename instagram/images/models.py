from django.db import models
from instagram.users import models as user_models

class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Image(TimeStampedModel):

    file        = models.ImageField()
    location    = models.CharField(max_length=140)
    caption     = models.TextField()
    creator     = models.ForeignKey(user_models.User, null=True, related_name='images')

    def __str__(self):
        return '{} - {}'.format(self.location, self.creator)


class Comment(TimeStampedModel):

    """" Comment Model """
    message = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True)
    image   = models.ForeignKey(Image, null=True, related_name='comments')

    def __str__(self):
        return '{} - {}'.format(self.message, self.creator)

class Like(TimeStampedModel):

    """" Like Model """
    creator = models.ForeignKey(user_models.User, null=True)
    image   = models.ForeignKey(Image, null=True, related_name='likes')

    def __str__(self):
        return '{} - {}'.format(self.image.caption, self.creator)


