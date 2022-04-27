# Generated by Django 3.2.5 on 2022-04-27 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sleep', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['headline'],
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.RemoveField(
            model_name='group',
            name='alarms',
        ),
        migrations.RemoveField(
            model_name='group',
            name='users',
        ),
        migrations.DeleteModel(
            name='Alarm',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='article',
            name='publications',
            field=models.ManyToManyField(to='sleep.Publication'),
        ),
    ]
