# Generated by Django 4.1.1 on 2022-09-25 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_drf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=10)),
            ],
        ),
    ]
