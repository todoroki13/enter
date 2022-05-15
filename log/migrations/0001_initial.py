# Generated by Django 3.1.4 on 2022-04-25 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admit', models.CharField(max_length=255, verbose_name='入學管道')),
                ('adesc', models.TextField(max_length=1023, verbose_name='說明')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart', models.CharField(max_length=255, verbose_name='科系/特殊班名稱')),
                ('ddesc', models.TextField(max_length=1023, verbose_name='說明')),
                ('d_file', models.FileField(upload_to='uploads/')),
                ('admits', models.ManyToManyField(to='log.Admission', verbose_name='入學管道')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='學校名稱')),
                ('sdesc', models.TextField(max_length=1023, verbose_name='說明')),
                ('type', models.IntegerField(choices=[(0, '高中'), (1, '高職'), (2, '五專'), (3, '綜高')], default=0, verbose_name='學校類型')),
                ('pp', models.IntegerField(choices=[(0, '公立'), (1, '私立')], default=0, verbose_name='公/私立')),
                ('departs', models.ManyToManyField(to='log.Department', verbose_name='科系')),
                ('getin', models.ManyToManyField(to='log.Admission', verbose_name='入學管道')),
            ],
        ),
    ]