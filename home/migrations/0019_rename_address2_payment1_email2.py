# Generated by Django 4.0.5 on 2022-09-10 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_payment1_phone3'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment1',
            old_name='address2',
            new_name='email2',
        ),
    ]
