# Generated by Django 4.2.6 on 2023-10-08 21:48

import asso.commons.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NavbarItem",
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
                ("slug", models.SlugField(max_length=100, unique=True)),
                ("title", models.CharField(max_length=100, verbose_name="Title")),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="A short description for this content (not visible in views)",
                        verbose_name="Description",
                    ),
                ),
                (
                    "show",
                    models.BooleanField(
                        default=True,
                        help_text="Set to False to hide this content in views",
                        verbose_name="Show",
                    ),
                ),
                (
                    "order",
                    models.SmallIntegerField(
                        default=0,
                        help_text="Object ordering value",
                        verbose_name="Order",
                    ),
                ),
                (
                    "url",
                    models.CharField(
                        default="",
                        max_length=200,
                        verbose_name="A URL or a relative path",
                    ),
                ),
            ],
            options={
                "ordering": ["slug"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SocialLink",
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
                ("title", models.CharField(max_length=100, verbose_name="Title")),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="A short description for this content (not visible in views)",
                        verbose_name="Description",
                    ),
                ),
                (
                    "show",
                    models.BooleanField(
                        default=True,
                        help_text="Set to False to hide this content in views",
                        verbose_name="Show",
                    ),
                ),
                (
                    "order",
                    models.SmallIntegerField(
                        default=0,
                        help_text="Object ordering value",
                        verbose_name="Order",
                    ),
                ),
                ("url", models.URLField()),
                (
                    "logo",
                    models.CharField(
                        choices=[
                            ("globe", "Web site (default)"),
                            ("facebook", "Facebook"),
                            ("twitter", "Twitter"),
                            ("x", "x.com"),
                            ("linkedin", "LinkedIn"),
                            ("youtube", "YouTube"),
                            ("github", "GitHub"),
                            ("instagram", "Instagram"),
                        ],
                        default="globe",
                        max_length=24,
                        verbose_name="Logo Icon",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ThemeConfig",
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
                ("default", asso.commons.fields.UniqueBooleanField(default=False)),
                ("brand", models.CharField(max_length=100)),
                ("logo", models.ImageField(blank=True, null=True, upload_to="logos")),
            ],
            options={
                "ordering": ["-default"],
                "abstract": False,
            },
        ),
    ]
