# Generated by Django 4.0.5 on 2022-08-27 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_name_admission_yname_alter_admission_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='gender',
            field=models.CharField(choices=[('others', 'others'), ('male', 'male'), ('female', 'female')], default='male', max_length=122),
        ),
    ]
