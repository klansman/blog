# Generated by Django 4.2.13 on 2024-12-07 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_reply_date_added_alter_reply_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='id',
            field=models.CharField(editable=False, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
