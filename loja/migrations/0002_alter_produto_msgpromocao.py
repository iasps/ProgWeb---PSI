# Generated by Django 5.0.7 on 2024-07-26 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='msgPromocao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]