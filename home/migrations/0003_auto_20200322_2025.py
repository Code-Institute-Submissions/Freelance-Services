# Generated by Django 2.2.2 on 2020-03-22 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200322_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='about',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='headline',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='subheadline',
            field=models.CharField(max_length=100),
        ),
    ]
