# Generated by Django 4.2.6 on 2023-11-21 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeentry', '0006_alter_period_begin_date_alter_period_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expert',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
