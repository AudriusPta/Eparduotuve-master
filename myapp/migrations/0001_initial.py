# Generated by Django 4.2.2 on 2023-07-03 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('discount_price', models.FloatField()),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=300)),
                ('Category_goods', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Category_goods', to='myapp.category_goods')),
            ],
        ),
    ]