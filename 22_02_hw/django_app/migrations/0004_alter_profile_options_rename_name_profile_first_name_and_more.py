# Generated by Django 4.2.2 on 2023-06-25 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0003_alter_profile_options_rename_user_profile_username_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ('id', 'user'), 'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='surname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(default='', max_length=20),
        ),
    ]