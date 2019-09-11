from django.db import models


class BlogQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status="published")

    def drafts(self):
        return self.filter(status="draft")


class BlogPost(models.Model):
    status = models.CharField(
        choices=[("draft", "Draft"), ("published", "Published")],
        default="draft",
        max_length=10,
    )
    title = models.CharField(max_length=200)
    body = models.TextField()

    objects = BlogQuerySet.as_manager()
