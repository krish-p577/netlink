# Generated by Django 4.2.14 on 2024-08-04 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createlinks', '0002_remove_linkset_biograpy_linkset_biography_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkset',
            name='linkone',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='linkset',
            name='linkthree',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='linkset',
            name='linktwo',
            field=models.CharField(max_length=30, null=True),
        ),
    ]