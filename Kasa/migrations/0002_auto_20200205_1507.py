# Generated by Django 2.2.9 on 2020-02-05 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kasa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='albums',
            name='aname',
            field=models.CharField(default='', max_length=255, verbose_name='앨범이름'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='songs',
            name='sname',
            field=models.CharField(default='', max_length=255, verbose_name='노래제목'),
            preserve_default=False,
        ),
    ]
