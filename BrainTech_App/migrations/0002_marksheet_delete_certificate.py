# Generated by Django 4.2.16 on 2024-09-22 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BrainTech_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marksheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.CharField(max_length=100, unique=True)),
                ('marksheet_image', models.ImageField(upload_to='marksheets/')),
            ],
        ),
        migrations.DeleteModel(
            name='Certificate',
        ),
    ]