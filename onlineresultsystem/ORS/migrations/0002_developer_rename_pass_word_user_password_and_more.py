# Generated by Django 5.0.1 on 2024-03-27 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ORS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('developer_name', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('project', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('submitting_date', models.DateField()),
            ],
            options={
                'db_table': 'ORS_developer',
            },
        ),
        migrations.RenameField(
            model_name='user',
            old_name='pass_word',
            new_name='password',
        ),
        migrations.AlterModelTable(
            name='user',
            table='ORS_USER',
        ),
    ]
