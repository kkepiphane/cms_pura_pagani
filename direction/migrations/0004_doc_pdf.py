# Generated by Django 3.2.4 on 2021-07-11 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direction', '0003_alter_depense_date_fin'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]