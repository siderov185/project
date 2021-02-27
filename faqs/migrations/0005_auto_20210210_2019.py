# Generated by Django 3.1.3 on 2021-02-10 18:19

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0004_auto_20210208_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='faqs',
            name='answer_bg',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faqs',
            name='answer_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faqs',
            name='question_bg',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faqs',
            name='question_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
