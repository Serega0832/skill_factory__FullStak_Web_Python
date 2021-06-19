# Generated by Django 3.2.4 on 2021-06-14 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=64)),
                ('is_completed', models.BooleanField(default=False, verbose_name='выполнено')),
            ],
        ),
    ]
