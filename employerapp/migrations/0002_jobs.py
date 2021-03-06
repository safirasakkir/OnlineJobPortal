# Generated by Django 4.0.4 on 2022-06-11 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=120)),
                ('job_description', models.TextField()),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('salary', models.PositiveIntegerField()),
                ('qualification', models.CharField(max_length=120, null=True)),
                ('experience', models.PositiveIntegerField(default=0)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
