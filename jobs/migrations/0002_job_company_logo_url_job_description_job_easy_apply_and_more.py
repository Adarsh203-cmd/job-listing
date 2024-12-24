# Generated by Django 5.1.4 on 2024-12-20 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company_logo_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='easy_apply',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='employer_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='is_highlighted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='is_remote',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='requirements',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
