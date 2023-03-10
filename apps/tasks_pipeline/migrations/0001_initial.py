# Generated by Django 4.1.7 on 2023-03-10 06:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monitoring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_class_ref', models.CharField(max_length=255)),
                ('model_instance_pk', models.IntegerField()),
                ('task_path', models.CharField(max_length=300)),
                ('task_arguments', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('new', 'new'), ('running', 'running'), ('success', 'success'), ('failed', 'failed')], default='new', max_length=50)),
                ('failed_reason', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pipeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('path', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='TaskArgument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('argument', models.CharField(max_length=100)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arguments', to='tasks_pipeline.task')),
            ],
        ),
        migrations.CreateModel(
            name='PipelineTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('pipeline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks_pipeline.pipeline')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks_pipeline.task')),
            ],
        ),
    ]
