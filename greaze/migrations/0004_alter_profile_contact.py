# Generated by Django 3.2.7 on 2021-09-16 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greaze', '0003_alter_rate_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact',
            field=models.CharField(blank=True, default=2547164482, max_length=10),
            preserve_default=False,
        ),
    ]
