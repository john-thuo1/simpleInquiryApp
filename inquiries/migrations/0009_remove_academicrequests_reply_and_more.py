# Generated by Django 4.2.5 on 2023-10-05 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inquiries", "0008_remove_academicreply_reply_date_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="academicrequests",
            name="reply",
        ),
        migrations.RemoveField(
            model_name="administrativerequests",
            name="reply",
        ),
        migrations.DeleteModel(
            name="AcademicReply",
        ),
        migrations.DeleteModel(
            name="AdministrativeReply",
        ),
        migrations.AddField(
            model_name="academicrequests",
            name="reply",
            field=models.TextField(
                default="No response yet",
                help_text="Enter a response to the Academic Request Above",
                max_length=2000,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="administrativerequests",
            name="reply",
            field=models.TextField(
                default="No Response Yet...",
                help_text="Enter a response to the Administrative Request Above",
                max_length=2000,
            ),
        ),
    ]
