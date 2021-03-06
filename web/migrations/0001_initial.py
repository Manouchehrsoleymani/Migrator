# Generated by Django 3.1 on 2020-08-04 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='attributes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255)),
                ('file_name', models.CharField(max_length=128)),
                ('size', models.BigIntegerField()),
                ('file_type', models.CharField(max_length=20)),
                ('create_time', models.DateTimeField()),
                ('modified_time', models.DateTimeField()),
                ('access_time', models.DateTimeField()),
            ],
        ),
    ]
