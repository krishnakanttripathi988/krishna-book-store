# Generated by Django 4.0.3 on 2022-03-25 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('book_name', models.CharField(max_length=200)),
                ('ID', models.CharField(default='', max_length=200, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('preview_link', models.URLField()),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]
