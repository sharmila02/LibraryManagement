# Generated by Django 4.0.6 on 2022-07-20 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_remove_issued_details_book_id_issued_details_book_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Issued_details',
        ),
    ]
