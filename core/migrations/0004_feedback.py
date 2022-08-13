# Generated by Django 4.0.6 on 2022-08-13 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_contact_alter_item_label'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(blank=True, max_length=100)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
    ]