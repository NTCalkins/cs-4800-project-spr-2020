# Generated by Django 2.2.11 on 2020-04-17 03:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import eaterie.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('is_customer', models.BooleanField(default=False, verbose_name='customer status')),
                ('is_restaurant', models.BooleanField(default=False, verbose_name='restaurant owner status')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', eaterie.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_address', models.CharField(blank=True, max_length=256)),
                ('phone_number', models.CharField(blank=True, max_length=10)),
                ('avatar', models.ImageField(blank=True, default='blank-profile-picture.png', upload_to='')),
                ('preference_1', models.CharField(choices=[('ITA', 'Italian'), ('FF', 'Fastfood'), ('CHN', 'Chinese'), ('VTN', 'Vietnamese')], default='ITA', max_length=64)),
                ('preference_2', models.CharField(choices=[('ITA', 'Italian'), ('FF', 'Fastfood'), ('CHN', 'Chinese'), ('VTN', 'Vietnamese')], default='VTN', max_length=64)),
                ('zip_code', models.CharField(blank=True, max_length=5)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name_plural': 'MenuCategories',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=80)),
                ('description', models.TextField(blank=True, max_length=512)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('image_file', models.ImageField(blank=True, default='no-image-available.png', upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eaterie.MenuCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('special_instruction', models.CharField(blank=True, max_length=512)),
                ('order_fulfilled', models.BooleanField(default=False)),
                ('order_cancelled', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eaterie.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_code', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='eaterie.Customer')),
                ('total_cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('menu_items', models.ManyToManyField(blank=True, to='eaterie.MenuItem')),
            ],
        ),
        migrations.CreateModel(
            name='ZipCode',
            fields=[
                ('zip_code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eaterie.City')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=80)),
                ('restaurant_address', models.CharField(blank=True, max_length=256)),
                ('phone_number', models.CharField(max_length=10)),
                ('image_file', models.ImageField(blank=True, default='no-image-available.png', upload_to='')),
                ('description', models.TextField(blank=True, max_length=256)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('zip_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eaterie.ZipCode')),
            ],
        ),
        migrations.AddField(
            model_name='menucategory',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eaterie.Restaurant'),
        ),
        migrations.AddField(
            model_name='city',
            name='state_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eaterie.State'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('menu_item', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='eaterie.MenuItem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eaterie.Order')),
            ],
            options={
                'unique_together': {('order', 'menu_item')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='menucategory',
            unique_together={('category_name', 'restaurant')},
        ),
        migrations.CreateModel(
            name='CartEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('menu_item', models.ForeignKey(null=True, on_delete='CASCADE', to='eaterie.MenuItem')),
                ('cart', models.ForeignKey(null=True, on_delete='CASCADE', to='eaterie.Cart')),
            ],
        ),
    ]
