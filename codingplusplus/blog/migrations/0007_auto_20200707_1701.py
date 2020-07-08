# Generated by Django 3.0.7 on 2020-07-07 11:31

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blogentrypage_templates'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPageCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=80, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.RemoveField(
            model_name='blogentrypage',
            name='templates',
        ),
        migrations.AddField(
            model_name='blogentrypage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(to='blog.BlogPageCategory'),
        ),
    ]
