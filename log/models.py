from django.db import models
from django.forms import IntegerField

# Create your models here.


class Admission(models.Model):

    admit = models.CharField('入學管道', max_length=256)
    adesc = models.TextField('說明', max_length=2048)
    afile = models.URLField('入學管道說明檔案', max_length=512, null=True, blank=True)

    def __str__(self):
        return self.admit


class School(models.Model):

    TYPE_OPTIONS = [
        (0, '高中'),
        (1, '高職'),
        (2, '五專'),
        (3, '綜高'),
    ]

    PP_OPTIONS = [
        (0, '公立'),
        (1, '私立'),
    ]

    name = models.CharField('學校名稱', max_length=256)
    sdesc = models.TextField('說明', max_length=2048)
    type = models.IntegerField('學校類型', default=0, choices=TYPE_OPTIONS)
    pp = models.IntegerField('公/私立', default=0, choices=PP_OPTIONS)
    sfile = models.URLField('學校說明檔案', max_length=512, null=True, blank=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    
    depart = models.CharField('科系/班級名稱', max_length=256)
    schools = models.ManyToManyField(School, related_name='departs')
    admits = models.ForeignKey(Admission, on_delete = models.CASCADE, null=True, verbose_name='入學管道')
    ddesc = models.TextField('說明', max_length=2048)
    dfile = models.URLField('科系/班級說明檔案', max_length=512, null=True, blank=True)

    def __str__(self):
        return self.depart

class Home(models.Model):

    htitle = models.CharField('網站消息標題', max_length=256)
    hdesc = models.TextField('網站消息內容', max_length=2048)