# Generated by Django 2.2.8 on 2020-04-07 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading_text', models.CharField(max_length=40)),
                ('date_and_time', models.DateTimeField(verbose_name='date published')),
                ('story_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='New_Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_text', models.CharField(max_length=200)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyExam.Article')),
            ],
        ),
    ]