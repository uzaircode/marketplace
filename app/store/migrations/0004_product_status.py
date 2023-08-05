# Generated by Django 3.2.20 on 2023-08-05 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20230804_0800'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('waitingapproval', 'Waiting approval'), ('active', 'Active'), ('deleted', 'Deleted')], default='active', max_length=50),
        ),
    ]
