# Generated by Django 4.1.1 on 2022-09-25 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iam_employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('emp_id', models.IntegerField()),
            ],
        ),
    ]
