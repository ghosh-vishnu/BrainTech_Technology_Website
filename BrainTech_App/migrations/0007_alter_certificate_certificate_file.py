# Generated by Django 4.2.16 on 2024-09-24 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BrainTech_App', '0006_certificate_certificate_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='certificate_file',
            field=models.FileField(blank=True, null=True, upload_to='certificates/'),
        ),
    ]
