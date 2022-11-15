# Generated by Django 3.1.3 on 2022-11-13 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('golf', '0011_auto_20221113_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='voter',
        ),
        migrations.RemoveField(
            model_name='question',
            name='voter',
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='golf.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
