from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Avg, Count

# Create your models here.


class Rating(models.Model):
    ip = models.GenericIPAddressField()
    post = models.ForeignKey(
        "Post",
        related_name="ratings",
        on_delete=models.CASCADE,
    )
    score = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["ip", "post"],
                name="unique rating",
            )
        ]


class Post(models.Model):
    # author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title

    @property
    def get_rating_counts(self):
        """Get all ratings counts for particular post."""
        return Rating.objects.filter(post=self.id).aggregate(count=Count("ip"))

    @property
    def get_rating_average(self):
        """Get average rating for particular post."""
        return Rating.objects.filter(post=self.id).aggregate(average=Avg("score"))
