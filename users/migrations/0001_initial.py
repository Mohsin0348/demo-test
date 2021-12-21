# Generated by Django 3.2.10 on 2021-12-19 06:30

import uuid

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import easy_thumbnails.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status')),
                ('last_active_on', models.DateTimeField(blank=True, null=True)),
                ('activation_token', models.UUIDField(blank=True, null=True)),
                ('deactivation_reason', models.TextField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_on', models.DateTimeField(blank=True, null=True)),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('member', 'Member'), ('employee', 'Employee')], default='member', max_length=16)),
                ('phone', models.CharField(blank=True, max_length=15, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='Enter Phone number with country code', regex='^\\+?1?\\d{9,15}$')], verbose_name='phone number')),
                ('is_phone_verified', models.BooleanField(default=False)),
                ('gender', models.CharField(blank=True, choices=[('female', 'Female'), ('male', 'Male'), ('others', 'Others')], max_length=8, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('photo', easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='profile_pictures/', verbose_name='ProfilePicture')),
                ('photo_uploaded_on', models.DateTimeField(blank=True, null=True)),
                ('is_profile_pic_verified', models.BooleanField(default=False)),
                ('rejection_reason_profile_pic', models.TextField(blank=True, null=True)),
                ('document_front', models.FileField(blank=True, null=True, upload_to='documents')),
                ('document_rear', models.FileField(blank=True, null=True, upload_to='documents')),
                ('document_uploaded_on', models.DateTimeField(blank=True, null=True)),
                ('document_expiry_date', models.DateField(blank=True, null=True)),
                ('is_document_verified', models.BooleanField(default=False)),
                ('rejection_reason_document', models.TextField(blank=True, null=True)),
                ('term_and_condition_accepted', models.BooleanField(default=False)),
                ('privacy_policy_accepted', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserDeviceToken',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('device_token', models.CharField(max_length=200)),
                ('device_type', models.CharField(choices=[('ios', 'Ios'), ('android', 'Android'), ('web', 'Web')], max_length=8)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UnitOfHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('old_meta', models.JSONField(null=True)),
                ('new_meta', models.JSONField(null=True)),
                ('header', models.JSONField(null=True)),
                ('object_id', models.CharField(max_length=100)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('perform_for', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='perform_for', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='performer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResetPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserSocialAccount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('social_id', models.CharField(max_length=100)),
                ('social_type', models.CharField(choices=[('facebook', 'Facebook'), ('google', 'Google'), ('apple', 'Apple')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'social_type')},
            },
        ),
        migrations.CreateModel(
            name='UserOTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(max_length=6)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_otp', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated_on'],
                'unique_together': {('user', 'otp')},
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(choices=[('permanent', 'Permanent'), ('present', 'Present'), ('business', 'Business'), ('office', 'Office')], default='present', max_length=32)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=128)),
                ('state', models.CharField(max_length=128)),
                ('postal_code', models.CharField(max_length=32)),
                ('country', models.CharField(max_length=128)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_addresses', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
                'unique_together': {('user', 'address_type')},
            },
        ),
    ]