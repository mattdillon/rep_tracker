# Generated by Django 2.1.4 on 2019-01-01 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gym_nm', models.CharField(max_length=200)),
                ('rec_ins_ts', models.DateTimeField()),
            ],
        ),
    ]
