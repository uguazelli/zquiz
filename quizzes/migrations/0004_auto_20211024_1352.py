# Generated by Django 3.2.8 on 2021-10-24 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0003_auto_20211024_0241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='quizz',
            new_name='quiz',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='quizz',
            new_name='quiz',
        ),
    ]
