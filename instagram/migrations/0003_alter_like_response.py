# Generated by Django 4.0.5 on 2022-06-08 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_alter_like_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='response',
            field=models.CharField(choices=[('Unlike', 'Unlike'), ('Like', 'Like')], default='like', max_length=70),
        ),
    ]
