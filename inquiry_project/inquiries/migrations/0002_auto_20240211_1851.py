# Generated by Django 3.2.21 on 2024-02-11 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subject_type', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=15)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='mobile_number',
            field=models.CharField(max_length=15),
        ),
    ]
