# Generated by Django 3.2.4 on 2021-06-15 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelWithCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('haircuts', 'Парикмахерские услуги'), ('nails', 'Маникюр'), ('eyebrows', 'Брови')], default='haircuts', max_length=32)),
            ],
        ),
    ]
