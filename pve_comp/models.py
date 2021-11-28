from accounts.models import User
from django.db import models
import uuid
from django.core.validators import MinValueValidator

class Chapter(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='章', validators=[MinValueValidator(1)])

    def __str__(self):
        return u'{}'.format(self.id)


class Stage(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ステージ', validators=[MinValueValidator(1)])

    def __str__(self):
        return u'{}'.format(self.id)


def rename_to_uuid(self, filename):
    prefix = 'comp/'
    return prefix + str(uuid.uuid4()).replace('-', '') + ".png"
    
class Post(models.Model):
    chapter_id = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    stage_id = models.ForeignKey(Stage, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_image = models.ImageField(upload_to=rename_to_uuid)
