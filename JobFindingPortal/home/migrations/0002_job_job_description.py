# Generated by Django 3.0.1 on 2020-02-10 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_description',
            field=models.FileField(default=None, upload_to='Job_Description'),
            preserve_default=False,
        ),
    ]
