# Generated by Django 4.2.1 on 2023-05-16 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0002_alter_answer_author_alter_question_author_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name_plural': 'Quizes'},
        ),
    ]
