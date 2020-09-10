# Generated by Django 3.1 on 2020-09-09 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20200827_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='entity_img',
            field=models.ImageField(blank=True, null=True, upload_to='static/polls/'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='entity_info',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='info',
            name='info_text',
            field=models.CharField(max_length=200),
        ),
    ]