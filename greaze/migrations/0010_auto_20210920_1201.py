# Generated by Django 3.2.7 on 2021-09-20 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greaze', '0009_alter_profile_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='content',
            field=models.IntegerField(choices=[(1, '1 - Trash'), (2, '2 - Horrible'), (3, '3 - Terrible'), (4, '4 - Bad'), (5, '5 - Ok'), (6, '6 - Watchable'), (7, '7 - Good'), (8, '8 - Very Good'), (9, '9 - Perfect'), (10, '10 - Master Piece')], default=0),
        ),
        migrations.AlterField(
            model_name='rate',
            name='design',
            field=models.PositiveSmallIntegerField(choices=[(1, '1 - Trash'), (2, '2 - Horrible'), (3, '3 - Terrible'), (4, '4 - Bad'), (5, '5 - Ok'), (6, '6 - Watchable'), (7, '7 - Good'), (8, '8 - Very Good'), (9, '9 - Perfect'), (10, '10 - Master Piece')], default=0),
        ),
        migrations.AlterField(
            model_name='rate',
            name='usability',
            field=models.IntegerField(choices=[(1, '1 - Trash'), (2, '2 - Horrible'), (3, '3 - Terrible'), (4, '4 - Bad'), (5, '5 - Ok'), (6, '6 - Watchable'), (7, '7 - Good'), (8, '8 - Very Good'), (9, '9 - Perfect'), (10, '10 - Master Piece')], default=0),
        ),
    ]
