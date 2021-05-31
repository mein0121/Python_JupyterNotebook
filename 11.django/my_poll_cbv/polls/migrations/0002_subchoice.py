# Generated by Django 3.2.3 on 2021-05-25 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubChoice',
            fields=[
                ('sub_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=2000)),
                ('sub_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.choice')),
            ],
        ),
    ]
