# Generated by Django 4.1.13 on 2023-12-23 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('company_type', models.CharField(choices=[('IT', 'IT'), ('Other', 'Other')], max_length=20)),
            ],
        ),
    ]
