# Generated by Django 4.1.3 on 2022-12-04 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_submission', '0004_remove_student_id_alter_student_student_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='student_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='submitassignment',
            name='student',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
