# Generated by Django 4.0.6 on 2022-07-13 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('approved', 'approved'), ('notapproved', 'notapproved')], default='notapproved', max_length=15)),
                ('register_date', models.DateField(auto_now_add=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='library.customuser')),
            ],
        ),
    ]
