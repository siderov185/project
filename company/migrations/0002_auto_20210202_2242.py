# Generated by Django 3.1.6 on 2021-02-02 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='politics',
            options={'verbose_name': 'Politic', 'verbose_name_plural': 'Politics'},
        ),
    ]