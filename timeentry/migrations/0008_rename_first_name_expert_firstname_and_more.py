# Generated by Django 4.2.6 on 2023-11-22 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeentry', '0007_alter_expert_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expert',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='expert',
            old_name='last_name',
            new_name='lastname',
        ),
        migrations.AlterField(
            model_name='case',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
