# Generated by Django 2.0 on 2018-04-02 02:33

from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('simlive', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('duration', models.IntegerField()),
                ('VideoList', django_mysql.models.ListTextField(models.IntegerField(), size=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProgramBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('duration', models.IntegerField()),
                ('DayBlockList', django_mysql.models.ListTextField(models.IntegerField(), size=20)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('video_id', models.CharField(max_length=20)),
                ('duration', models.IntegerField()),
                ('description', models.TextField()),
                ('path', models.CharField(max_length=200)),
                ('bcAccount', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='simlive.BCAccount')),
            ],
        ),
    ]
