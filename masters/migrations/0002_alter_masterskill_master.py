# Generated by Django 3.2.4 on 2021-06-15 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterskill',
            name='master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='masters.master', verbose_name='Мастер'),
        ),
    ]
