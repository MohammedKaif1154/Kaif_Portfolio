# Generated by Django 5.1.2 on 2025-01-18 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("resume", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contact",
            old_name="message",
            new_name="messsage",
        ),
    ]
