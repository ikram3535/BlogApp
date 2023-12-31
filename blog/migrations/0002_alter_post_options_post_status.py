# Generated by Django 4.2.3 on 2023-07-17 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post", options={"ordering": ["-publishing_date", "id"]},
        ),
        migrations.AddField(
            model_name="post",
            name="status",
            field=models.CharField(
                choices=[
                    ("software", "yazilim"),
                    ("product", "urun"),
                    ("game", "oyun"),
                    ("book", "kitab"),
                    ("movie", "film"),
                ],
                default="software",
                max_length=10,
            ),
        ),
    ]
