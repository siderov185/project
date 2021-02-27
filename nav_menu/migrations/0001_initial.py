# Generated by Django 3.1.3 on 2021-02-08 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NavMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField(max_length=150)),
                ('is_first_level', models.BooleanField(default=True)),
                ('order', models.CharField(blank=True, max_length=100, null=True)),
                ('children', models.ManyToManyField(blank=True, related_name='_navmenu_children_+', to='nav_menu.NavMenu')),
            ],
        ),
    ]
