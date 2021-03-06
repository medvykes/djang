# Generated by Django 3.1.6 on 2021-02-23 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Speech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('speech_date', models.DateField(blank=True)),
                ('speeech', models.TextField(max_length=2000)),
                ('speaker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='spoke.speaker')),
            ],
            options={
                'ordering': ['title', 'speech_date', 'speaker'],
            },
        ),
    ]
