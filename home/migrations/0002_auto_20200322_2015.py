# Generated by Django 2.2.2 on 2020-03-22 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('headline', models.CharField(max_length=20)),
                ('subheadline', models.CharField(max_length=50)),
                ('about', models.TextField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='About',
        ),
    ]
