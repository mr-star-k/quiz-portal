# Generated by Django 2.0.6 on 2018-06-06 17:22

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=225)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruction', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', ckeditor_uploader.fields.RichTextUploadingField()),
                ('choice1', ckeditor_uploader.fields.RichTextUploadingField()),
                ('choice2', ckeditor_uploader.fields.RichTextUploadingField()),
                ('choice3', ckeditor_uploader.fields.RichTextUploadingField()),
                ('choice4', ckeditor_uploader.fields.RichTextUploadingField()),
                ('correct_choice', models.IntegerField()),
                ('negative', models.BooleanField(default=False)),
                ('negative_marks', models.IntegerField(null=True)),
                ('marks', models.IntegerField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=100)),
                ('duration', models.PositiveIntegerField()),
            ],
        ),
    ]
