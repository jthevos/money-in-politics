# Generated by Django 3.0.5 on 2020-04-16 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Legislator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(max_length=8)),
                ('firstlast', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('party', models.CharField(max_length=1)),
                ('office', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=1)),
            ],
        ),
    ]
