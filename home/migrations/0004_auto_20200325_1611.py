# Generated by Django 2.2.2 on 2020-03-25 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200322_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='first_skill_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='first_skill_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='homepage',
            name='second_skill_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='second_skill_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='homepage',
            name='third_skill_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='third_skill_name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]