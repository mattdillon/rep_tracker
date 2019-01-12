# Generated by Django 2.1.4 on 2019-01-12 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_nm', models.CharField(max_length=200)),
                ('rec_ins_ts', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ex_type_cd', models.CharField(max_length=2)),
                ('ex_type_desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gym_nm', models.CharField(max_length=200)),
                ('rec_ins_ts', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rec_ins_ts', models.DateTimeField()),
                ('user_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_ts', models.DateTimeField()),
                ('end_ts', models.DateTimeField(blank=True, null=True)),
                ('gym', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workouts.Gym')),
                ('individual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts.Individual')),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reps', models.IntegerField(default=0)),
                ('weight', models.IntegerField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts.Exercise')),
                ('session', models.ForeignKey(default=999, on_delete=django.db.models.deletion.CASCADE, to='workouts.Session')),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='ex_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts.ExerciseType'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='indiv_create',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts.Individual'),
        ),
    ]
