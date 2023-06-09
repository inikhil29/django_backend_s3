# Generated by Django 4.1.4 on 2023-06-30 11:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUploadModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(default='', max_length=255)),
                ('status', models.IntegerField(choices=[(0, 'Not Uploaded'), (1, 'Uploaded')], default=0)),
                ('creation_timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='UploadedFileDetailsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('file_path', models.CharField(max_length=255)),
                ('creation_timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('delete_flag', models.SmallIntegerField(choices=[(0, 'Not Deleted'), (1, 'Deleted')], default=0)),
                ('upload_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file_operation.fileuploadmodel')),
            ],
        ),
    ]
