# Generated by Django 5.1.7 on 2025-04-17 05:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('video', models.FileField(blank=True, upload_to='uploads/videolar/', verbose_name='Video')),
                ('word', models.FileField(blank=True, upload_to='uploads/laboratoriya_word/', verbose_name='Laboratoriya word')),
                ('presentation', models.FileField(blank=True, upload_to='uploads/presentations/laboratoriya/', verbose_name='Laboratoriya taqdimot')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Laboratoriya',
                'verbose_name_plural': 'Laboratoriyalar',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('video', models.FileField(blank=True, upload_to='uploads/videolar/', verbose_name='Video')),
                ('word', models.FileField(blank=True, upload_to='uploads/maruza_word/', verbose_name="Ma'ruza word")),
                ('presentation', models.FileField(blank=True, upload_to="uploads/presentations/ma'ruza/", verbose_name="Ma'ruza taqdimot")),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': "Ma'ruza",
                'verbose_name_plural': "Ma'ruzalar",
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('video', models.FileField(blank=True, upload_to='uploads/videolar/', verbose_name='Video')),
                ('word', models.FileField(blank=True, upload_to='uploads/amaliyot_word/', verbose_name='Amaliyot word')),
                ('presentation', models.FileField(blank=True, upload_to='uploads/presentations/amaliyot/', verbose_name='Amaliyot taqdimot')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Amaliyot',
                'verbose_name_plural': 'Amaliyotlar',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='subject.lecture')),
            ],
            options={
                'verbose_name': 'Test',
                'verbose_name_plural': 'Testlar',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='TestOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('is_correct', models.BooleanField(default=False)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='subject.test')),
            ],
            options={
                'verbose_name': 'Variant',
                'verbose_name_plural': 'Variantlar',
            },
        ),
    ]
