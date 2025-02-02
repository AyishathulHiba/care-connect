# Generated by Django 5.0 on 2024-09-06 09:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0020_prescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('feedback', models.CharField(max_length=500)),
                ('date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product_image/')),
                ('price', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('order_date', models.DateField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Order Confirmed', 'Order Confirmed'), ('Delivered', 'Delivered')], max_length=50, null=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.product')),
            ],
        ),
    ]
