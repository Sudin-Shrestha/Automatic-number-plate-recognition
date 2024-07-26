# Generated by Django 4.0.2 on 2022-02-14 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0008_alter_numberplate_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to='images/')),
                ('videofile', models.FileField(upload_to='videos/')),
            ],
        ),
        migrations.RemoveField(
            model_name='numberplate',
            name='img',
        ),
        migrations.RemoveField(
            model_name='numberplate',
            name='videofile',
        ),
    ]
