# Generated by Django 5.0.6 on 2024-06-12 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issueitem',
            old_name='amount',
            new_name='issued_amount',
        ),
    ]
