# Generated by Django 5.0 on 2023-12-08 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseekerapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=20),
        ),
    ]
