# Generated by Django 3.0.7 on 2021-06-24 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_delete_auth_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='auth_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('password1', models.CharField(max_length=20)),
                ('password2', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]