# Generated by Django 5.0.1 on 2024-03-26 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('developer_name', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('project', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('submitting_date', models.DateField(max_length=50)),
            ],
        ),
    ]
