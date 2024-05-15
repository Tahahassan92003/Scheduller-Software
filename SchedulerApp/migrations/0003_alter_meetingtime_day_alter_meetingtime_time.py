# Generated by Django 5.0.4 on 2024-04-25 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchedulerApp', '0002_section_num_class_in_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingtime',
            name='day',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=15),
        ),
        migrations.AlterField(
            model_name='meetingtime',
            name='time',
            field=models.CharField(choices=[('8:45 - 9:45', '8:45 - 9:45'), ('10:00 - 11:00', '10:00 - 11:00'), ('11:00 - 12:00', '11:00 - 12:00'), ('1:00 - 2:00', '1:00 - 2:00'), ('2:15 - 3:15', '2:15 - 3:15')], default='11:30 - 12:30', max_length=50),
        ),
    ]