# Generated by Django 3.1.5 on 2021-02-05 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('year', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=63)),
                ('address', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('role', models.CharField(choices=[('P', 'participant'), ('E', 'expert'), ('O', 'organizer')], default='P', max_length=1)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=25)),
                ('video_path', models.URLField(blank=True, null=True)),
                ('info', models.CharField(blank=True, max_length=255, null=True)),
                ('score', models.IntegerField(default=0)),
                ('leader_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yeti_app.participant')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('password', models.CharField(max_length=127)),
                ('mail', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=127)),
                ('phone', models.CharField(max_length=12)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='user_photos')),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yeti_app.participant')),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yeti_app.team')),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='team_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='yeti_app.team'),
        ),
        migrations.AddField(
            model_name='participant',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yeti_app.user'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='team_images')),
                ('comment', models.CharField(max_length=255)),
                ('team_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='yeti_app.team')),
            ],
        ),
        migrations.CreateModel(
            name='Blueprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blueprint', models.ImageField(upload_to='team_blueprints')),
                ('info', models.CharField(max_length=255)),
                ('team_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='yeti_app.team')),
            ],
        ),
    ]
