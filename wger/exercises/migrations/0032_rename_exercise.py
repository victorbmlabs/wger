# Generated by Django 4.2.13 on 2024-07-08 17:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('exercises', '0030_increase_author_field_length'),
        ('manager', '0017_alter_workoutlog_exercise_base'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Exercise',
            new_name='Translation',
        ),
        migrations.RenameModel(
            old_name='HistoricalExercise',
            new_name='HistoricalTranslation',
        ),
        migrations.RenameModel(
            old_name='ExerciseBase',
            new_name='Exercise',
        ),
        migrations.RenameModel(
            old_name='HistoricalExerciseBase',
            new_name='HistoricalExercise',
        ),
    ]