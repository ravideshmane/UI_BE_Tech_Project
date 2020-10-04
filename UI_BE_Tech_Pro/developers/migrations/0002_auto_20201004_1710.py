# Generated by Django 3.0 on 2020-10-04 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20201004_1548'),
        ('developers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developers',
            name='designation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.Designation'),
        ),
        migrations.AlterField(
            model_name='developers',
            name='employment_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.EmploymentType'),
        ),
        migrations.AlterField(
            model_name='developers',
            name='tech_stack',
            field=models.ManyToManyField(blank=True, null=True, to='common.TechStack'),
        ),
        migrations.AlterField(
            model_name='developers',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.User'),
        ),
    ]
