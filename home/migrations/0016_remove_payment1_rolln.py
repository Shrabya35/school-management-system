# Generated by Django 4.0.5 on 2022-09-10 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_rename_subj_admin1_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment1',
            name='rolln',
        ),
    ]