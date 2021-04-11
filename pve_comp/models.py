from os import times
from typing import ClassVar
from django.db import models
from django.db.models.query_utils import RegisterLookupMixin, select_related_descend
from django.utils import timezone
import uuid

def rename_to_uuid(self, filename):
    prefix = 'comp/'
    return prefix + str(uuid.uuid4()).replace('-', '') + ".png"

class ChapterStage(models.Model):
    chapter = models.CharField(max_length=4)
    stage = models.CharField(max_length=4)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_image = models.ImageField(upload_to=rename_to_uuid)

    def __str__(self):
        return f'{self.chapter} {self.stage}'
