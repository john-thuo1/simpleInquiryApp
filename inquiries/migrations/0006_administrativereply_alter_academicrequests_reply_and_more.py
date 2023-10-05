# Generated by Django 4.2.5 on 2023-10-05 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("inquiries", "0005_remove_academicreply_academic_request"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdministrativeReply",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField(max_length=2000)),
                ("reply_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name="academicrequests",
            name="reply",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="inquiries.academicreply",
            ),
        ),
        migrations.AddField(
            model_name="administrativerequests",
            name="reply",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="inquiries.administrativereply",
            ),
        ),
    ]