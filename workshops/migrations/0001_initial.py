# Generated by Django 2.2.6 on 2019-10-10 07:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('facilitators', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('venue', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('team', models.IntegerField(default=0)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('workshop_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('facilitator', models.ForeignKey(default='Anonymous', on_delete=django.db.models.deletion.DO_NOTHING, to='facilitators.Facilitator')),
            ],
        ),
    ]
