# Generated by Django 5.1.2 on 2024-11-18 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0003_remove_historicaljobopportunity_institution_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicaljobopportunity",
            name="company_name",
            field=models.CharField(
                blank=True,
                help_text="Enter the name of the company.",
                max_length=255,
                null=True,
                verbose_name="Company Name",
            ),
        ),
        migrations.AlterField(
            model_name="jobopportunity",
            name="company_name",
            field=models.CharField(
                blank=True,
                help_text="Enter the name of the company.",
                max_length=255,
                null=True,
                verbose_name="Company Name",
            ),
        ),
    ]