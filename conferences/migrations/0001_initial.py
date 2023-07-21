# Generated by Django 4.2.3 on 2023-07-18 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('venue', models.CharField(max_length=255)),
                ('theme', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('contact_info', models.CharField(max_length=255)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='speakers/')),
                ('areas_of_expertise', models.TextField()),
            ],
        ),
    ]
