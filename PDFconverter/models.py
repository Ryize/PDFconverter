import os

from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='files/%Y/%m/%d/')
    data = models.DateField(verbose_name='Дата', auto_now_add=True)

    def get_file_size(self):
        return os.path.getsize(self.file.path)

    def get_file_path_extension(self):
        return os.path.splitext(self.file.path)

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'