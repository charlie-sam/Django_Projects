# Generated by Django 3.2.21 on 2024-02-16 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiries', '0005_remove_enquiry_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]