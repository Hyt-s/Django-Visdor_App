# Generated by Django 3.2.3 on 2021-11-04 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_brach_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default='default.png', upload_to='teacher'),
        ),
    ]