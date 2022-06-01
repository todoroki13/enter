from django.db import models
from django.forms import IntegerField
from datetime import date

# Create your models here.


class Admission(models.Model):

    admit = models.CharField('入學方法', max_length=256)
    adesc = models.TextField('入學方法說明(選填)', max_length=2048, null=True, blank=True)
    afile = models.URLField('入學方法說明檔案Google雲端網址(選填)', max_length=512, null=True, blank=True)
    alink1name = models.CharField('入學方法參考網址名稱1(先選填)', max_length=256, null=True, blank=True)
    alink1 = models.URLField('入學方法參考網址1(先選填)', max_length=512, null=True, blank=True)
    alink2name = models.CharField('入學方法參考網址名稱2(後選填)', max_length=256, null=True, blank=True)
    alink2 = models.URLField('入學方法參考網址2(後選填)', max_length=512, null=True, blank=True)

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
    sdesc = models.TextField('學校說明(選填)', max_length=2048, null=True, blank=True)
    type = models.IntegerField('學校類型', default=0, choices=TYPE_OPTIONS)
    pp = models.IntegerField('公/私立', default=0, choices=PP_OPTIONS)
    sfile = models.URLField('學校說明檔案Google雲端網址(選填)', max_length=512, null=True, blank=True)
    slink1name = models.CharField('學校參考網址名稱1(先選填)', max_length=256, null=True, blank=True)
    slink1 = models.URLField('學校參考網址1(先選填)', max_length=512, null=True, blank=True)
    slink2name = models.CharField('學校參考網址名稱2(後選填)', max_length=256, null=True, blank=True)
    slink2 = models.URLField('學校參考網址2(後選填)', max_length=512, null=True, blank=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    
    depart = models.CharField('科系/班級名稱', max_length=256)
    schools = models.ManyToManyField(School, related_name='departs', verbose_name='學校')
    admits = models.ForeignKey(Admission, on_delete = models.CASCADE, null=True, verbose_name='入學方法')
    ddesc = models.TextField('說明(選填)', max_length=2048, null=True, blank=True)
    dfile = models.URLField('科系/班級說明檔案Google雲端網址(選填)', max_length=512, null=True, blank=True)
    dlink1name = models.CharField('科系/班級參考網址名稱1(先選填)', max_length=256, null=True, blank=True)
    dlink1 = models.URLField('科系/班級參考網址1(先選填)', max_length=512, null=True, blank=True)
    dlink2name = models.CharField('科系/班級參考網址名稱2(後選填)', max_length=256, null=True, blank=True)
    dlink2 = models.URLField('科系/班級參考網址2(後選填)', max_length=512, null=True, blank=True)

    def __str__(self):
        return self.depart

class Home(models.Model):

    htitle = models.CharField('網站消息標題', max_length=256)
    hdesc = models.TextField('網站消息內容', max_length=2048)
    htime = models.DateField('新增時間', default=date.today)
    hlink1name = models.CharField('消息參考網址名稱1(先選填)', max_length=256, null=True, blank=True)
    hlink1 = models.URLField('消息參考網址1(先選填)', max_length=512, null=True, blank=True)
    hlink2name = models.CharField('消息參考網址名稱2(後選填)', max_length=256, null=True, blank=True)
    hlink2 = models.URLField('消息參考網址2(後選填)', max_length=512, null=True, blank=True)