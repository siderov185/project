# Generated by Django 3.1.3 on 2021-02-10 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contactmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='company_bg',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='company_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='title_bg',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
