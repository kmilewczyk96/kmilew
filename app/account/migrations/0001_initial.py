# Generated by Django 4.0.5 on 2022-06-09 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=48)),
                ('home_img', models.ImageField(blank=True, null=True, upload_to='profiles/<django.db.models.fields.UUIDField>/')),
                ('description', models.TextField(blank=True, max_length=256, null=True)),
                ('link_github', models.CharField(blank=True, max_length=128, null=True)),
                ('link_linkedin', models.CharField(blank=True, max_length=128, null=True)),
                ('link_twitter', models.CharField(blank=True, max_length=128, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
