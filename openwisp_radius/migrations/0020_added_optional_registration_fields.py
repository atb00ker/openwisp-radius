# Generated by Django 3.1.5 on 2021-01-14 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openwisp_radius', '0019_made_phonetoken_phone_number_required'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationradiussettings',
            name='birth_date',
            field=models.CharField(
                blank=True,
                choices=[
                    ('disabled', 'Disabled'),
                    ('allowed', 'Allowed'),
                    ('mandatory', 'Mandatory'),
                ],
                help_text=(
                    'Chose if this user field should be disabled, '
                    'allowed or mandatory during user registration.'
                ),
                max_length=12,
                null=True,
                verbose_name='birth date',
            ),
        ),
        migrations.AddField(
            model_name='organizationradiussettings',
            name='first_name',
            field=models.CharField(
                blank=True,
                choices=[
                    ('disabled', 'Disabled'),
                    ('allowed', 'Allowed'),
                    ('mandatory', 'Mandatory'),
                ],
                help_text=(
                    'Chose if this user field should be disabled, '
                    'allowed or mandatory during user registration.'
                ),
                max_length=12,
                null=True,
                verbose_name='first name',
            ),
        ),
        migrations.AddField(
            model_name='organizationradiussettings',
            name='last_name',
            field=models.CharField(
                blank=True,
                choices=[
                    ('disabled', 'Disabled'),
                    ('allowed', 'Allowed'),
                    ('mandatory', 'Mandatory'),
                ],
                help_text=(
                    'Chose if this user field should be disabled, '
                    'allowed or mandatory during user registration.'
                ),
                max_length=12,
                null=True,
                verbose_name='last name',
            ),
        ),
        migrations.AddField(
            model_name='organizationradiussettings',
            name='location',
            field=models.CharField(
                blank=True,
                choices=[
                    ('disabled', 'Disabled'),
                    ('allowed', 'Allowed'),
                    ('mandatory', 'Mandatory'),
                ],
                help_text=(
                    'Chose if this user field should be disabled, '
                    'allowed or mandatory during user registration.'
                ),
                max_length=12,
                null=True,
                verbose_name='location',
            ),
        ),
    ]
