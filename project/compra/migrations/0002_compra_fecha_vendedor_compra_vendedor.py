# Generated by Django 5.0.6 on 2024-05-14 00:11

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatares')),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vendedor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'vendedor',
                'verbose_name_plural': 'vendedores',
            },
        ),
        migrations.AddField(
            model_name='compra',
            name='vendedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='compra.vendedor', verbose_name='vendedor'),
        ),
    ]
