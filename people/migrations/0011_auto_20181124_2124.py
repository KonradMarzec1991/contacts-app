# Generated by Django 2.1.3 on 2018-11-24 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0010_merge_20181124_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='people',
            field=models.ManyToManyField(related_name='address', to='people.Person'),
        ),
    ]
