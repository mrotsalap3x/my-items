# Generated by Django 3.2.3 on 2021-05-18 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('needs_update', models.BooleanField(default=False)),
                ('has_subs', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last updated')),
                ('title', models.CharField(max_length=200)),
                ('order_no', models.SmallIntegerField(default=0)),
                ('contained_in', models.ManyToManyField(blank=True, related_name='_my_item_location_contained_in_+', to='my_item.Location')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('needs_update', models.BooleanField(default=False)),
                ('has_subs', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last updated')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('contained_in', models.ManyToManyField(blank=True, related_name='_my_item_item_contained_in_+', to='my_item.Item')),
                ('stored_in', models.ManyToManyField(blank=True, to='my_item.Location')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]