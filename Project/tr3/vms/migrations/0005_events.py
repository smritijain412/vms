# Generated by Django 3.1.4 on 2021-01-16 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0004_visit'),
    ]

    operations = [
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=250)),
                ('event_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
