# Generated by Django 5.1.4 on 2025-01-03 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_propertydetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
