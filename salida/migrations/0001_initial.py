# Generated by Django 3.0.2 on 2020-01-31 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('email_verified_at', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('documento', models.CharField(max_length=200)),
                ('celular', models.CharField(max_length=200)),
                ('fecha_nacimiento', models.CharField(max_length=200)),
                ('remember_token', models.CharField(max_length=200)),
                ('created_at', models.CharField(max_length=200)),
                ('updated_at', models.CharField(max_length=200)),
            ],
        ),
    ]
