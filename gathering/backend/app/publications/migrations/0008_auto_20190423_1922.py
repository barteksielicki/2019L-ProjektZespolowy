# Generated by Django 2.1.7 on 2019-04-23 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0007_auto_20190423_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotation',
            name='annotation_used',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='publications.Annotation'),
        ),
        migrations.AddField(
            model_name='annotation',
            name='is_used',
            field=models.BooleanField(default=False),
        ),
    ]
