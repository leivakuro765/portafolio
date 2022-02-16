# Generated by Django 4.0.2 on 2022-02-16 17:53

from django.db import migrations, models
import django_editorjs.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Titulo')),
                ('body', django_editorjs.fields.EditorJsField()),
            ],
        ),
    ]
