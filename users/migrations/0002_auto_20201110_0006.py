# Generated by Django 3.1.2 on 2020-11-10 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='spouse_name',
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.IntegerField(choices=[(0, 'Male'), (1, 'Female')], default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
