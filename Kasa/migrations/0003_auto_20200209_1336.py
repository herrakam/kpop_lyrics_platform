# Generated by Django 2.2.9 on 2020-02-09 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kasa', '0002_auto_20200205_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lyrics',
            name='singer',
            field=models.ManyToManyField(blank=True, related_name='singer_lyrics', to='Kasa.Singers', verbose_name='파트'),
        ),
    ]
