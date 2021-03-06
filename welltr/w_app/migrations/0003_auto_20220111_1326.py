# Generated by Django 3.2.11 on 2022-01-11 13:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('w_app', '0002_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='steps',
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steps', models.IntegerField(blank=True, default=0, null=True, verbose_name='количество шагов')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='время')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data', to='w_app.user', verbose_name='Данные')),
            ],
            options={
                'verbose_name': 'Данные',
                'verbose_name_plural': 'Данные',
            },
        ),
    ]
