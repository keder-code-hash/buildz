# Generated by Django 3.2 on 2023-01-28 13:27

from django.db import migrations, models
import django.db.models.deletion
import project.models.AreaModel


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_created=True, auto_now=True)),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('notes', models.CharField(blank=True, max_length=255, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AreaImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_created=True, auto_now=True)),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('image_name', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(upload_to=project.models.AreaModel.area_image_directory_path)),
                ('pinned_point_loc_x', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('pinned_point_loc_y', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('image_min_x', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('image_max_x', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('image_min_y', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('image_max_y', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_created=True, auto_now=True)),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('CL', 'Commercial'), ('IL', 'Industrial'), ('RL', 'Residential')], default='CL', max_length=2)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('timeline', models.CharField(choices=[('ASAP', 'ASAP'), ('Within the next Week/Few Weeks', 'Within the next Week/Few Weeks'), ('Within the next Month/Few Months', 'Within the next Month/Few Months')], default='ASAP', max_length=80)),
                ('status', models.CharField(choices=[('ong', 'Ongoing'), ('compl', 'Completed')], default='ong', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='AskedQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_created=True, auto_now=True)),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('question', models.CharField(blank=True, max_length=255, null=True)),
                ('answer', models.CharField(blank=True, max_length=255, null=True)),
                ('related_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_area', to='project.area')),
            ],
        ),
        migrations.AddField(
            model_name='area',
            name='related_image',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='project.areaimage'),
        ),
    ]
