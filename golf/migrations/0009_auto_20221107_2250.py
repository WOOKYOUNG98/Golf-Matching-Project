# Generated by Django 3.1.3 on 2022-11-07 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golf', '0008_auto_20221107_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='create_date',
            field=models.DateTimeField(),
        ),
    ]
