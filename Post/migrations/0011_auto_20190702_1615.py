# Generated by Django 2.2.3 on 2019-07-02 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0010_auto_20190702_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(default='post_img/default.png', upload_to='post_img/'),
        ),
    ]
