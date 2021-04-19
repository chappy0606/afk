from django.db import models
import uuid


class Chapter(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='章')

    def __str__(self):
        return u'{}'.format(self.id)


class Stage(models.Model):
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return u'{}'.format(self.id)


def rename_to_uuid(self, filename):
    prefix = 'comp/'
    return prefix + str(uuid.uuid4()).replace('-', '') + ".png"


class ChapterStage(models.Model):
    chapter_id = models.ForeignKey(Chapter, on_delete=models.CASCADE, default=1)
    stage_id = models.ForeignKey(Stage, on_delete=models.CASCADE, default=1)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_image = models.ImageField(upload_to=rename_to_uuid)
    # user_name = models.ForeignKey(User, on_delete=models.CASCADE
