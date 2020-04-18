# Generated by Django 3.0.5 on 2020-04-18 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('open_secrets', '0002_auto_20200418_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legislator',
            name='bioguide_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='birthdate',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='congress_office',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='facebook_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='fax',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='feccandid',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='first_elected',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='lastname',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='office',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='phone',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='twitter_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='votesmart_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='webform',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='website',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='youtube_url',
            field=models.CharField(default='', max_length=200),
        ),
    ]