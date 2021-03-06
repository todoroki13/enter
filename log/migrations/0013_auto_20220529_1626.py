# Generated by Django 3.1.4 on 2022-05-29 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0012_auto_20220529_0207'),
    ]

    operations = [
        migrations.AddField(
            model_name='admission',
            name='alink1name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='入學方法參考網址名稱(先選填)'),
        ),
        migrations.AddField(
            model_name='admission',
            name='alink2name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='入學方法參考網址名稱(後選填)'),
        ),
        migrations.AddField(
            model_name='department',
            name='dlink1name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='科系/班級參考網址名稱(先選填)'),
        ),
        migrations.AddField(
            model_name='department',
            name='dlink2name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='科系/班級參考網址名稱(後選填)'),
        ),
        migrations.AddField(
            model_name='school',
            name='slink1name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='學校參考網址名稱(先選填)'),
        ),
        migrations.AddField(
            model_name='school',
            name='slink2name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='學校參考網址名稱(後選填)'),
        ),
    ]
