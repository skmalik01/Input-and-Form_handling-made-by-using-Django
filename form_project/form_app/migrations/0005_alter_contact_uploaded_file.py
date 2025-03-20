# Generated by Django 5.1.7 on 2025-03-20 05:21

import django.core.validators
import form_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0004_delete_uploadedfile_contact_uploaded_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='uploaded_file',
            field=models.FileField(blank=True, null=True, upload_to=form_app.models.upload_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])]),
        ),
    ]
