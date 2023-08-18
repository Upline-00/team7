# Generated by Django 4.2.4 on 2023-08-11 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('askapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='create_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='create_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='subject',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]