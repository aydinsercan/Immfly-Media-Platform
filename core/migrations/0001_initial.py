# Generated by Django 3.1.3 on 2023-03-08 14:13

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('language', models.CharField(max_length=2)),
                ('picture', models.ImageField(upload_to='channels')),
                ('parent_channel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subchannels', to='core.channel')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('metadata', jsonfield.fields.JSONField()),
                ('text', models.TextField()),
                ('rating', models.IntegerField()),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.channel')),
            ],
        ),
    ]
