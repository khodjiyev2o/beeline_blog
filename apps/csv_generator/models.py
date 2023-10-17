from django.db import models
from apps.common.models import BaseModel
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Blog(BaseModel):
    title = models.CharField(verbose_name=_("Title"), max_length=255)
    content = models.TextField(verbose_name=_("Content"), max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Author"))
    image = models.ImageField(upload_to="blog/images/%Y/%m/", verbose_name=_("Image"))

    def __str__(self):
        return f"{self.title} - {self.author.username}"

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")
        ordering = ("-created_at", )
