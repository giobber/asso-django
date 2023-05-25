# Generated by Django 4.2.1 on 2023-05-25 00:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("academy", "0011_event_end_date_event_start_date"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="approvalstate",
            options={"ordering": ["-creation_date"]},
        ),
        migrations.RemoveField(
            model_name="approvalstate",
            name="name",
        ),
        migrations.RemoveField(
            model_name="approvalstate",
            name="trash_state",
        ),
        migrations.RemoveField(
            model_name="approvalstate",
            name="updated_by",
        ),
        migrations.RemoveField(
            model_name="enrollment",
            name="updated_by",
        ),
        migrations.RemoveField(
            model_name="event",
            name="trash_state",
        ),
        migrations.RemoveField(
            model_name="event",
            name="updated_by",
        ),
        migrations.RemoveField(
            model_name="presence",
            name="updated_by",
        ),
        migrations.RemoveField(
            model_name="session",
            name="updated_by",
        ),
        migrations.RemoveField(
            model_name="trainer",
            name="trash_state",
        ),
        migrations.RemoveField(
            model_name="trainer",
            name="updated_by",
        ),
        migrations.AddField(
            model_name="approvalstate",
            name="edit_by",
            field=models.ForeignKey(
                blank=True,
                help_text="The User who last edited this %(class)",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_updated_by",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Last edit User",
            ),
        ),
        migrations.AddField(
            model_name="approvalstate",
            name="is_trashed",
            field=models.BooleanField(
                default=False, help_text="Is the object trashed", verbose_name="Trashed"
            ),
        ),
        migrations.AddField(
            model_name="approvalstate",
            name="title",
            field=models.CharField(default="", max_length=256, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="enrollment",
            name="edit_by",
            field=models.ForeignKey(
                blank=True,
                help_text="The User who last edited this %(class)",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_updated_by",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Last edit User",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="edit_by",
            field=models.ForeignKey(
                blank=True,
                help_text="The User who last edited this %(class)",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_updated_by",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Last edit User",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="is_trashed",
            field=models.BooleanField(
                default=False, help_text="Is the object trashed", verbose_name="Trashed"
            ),
        ),
        migrations.AddField(
            model_name="presence",
            name="edit_by",
            field=models.ForeignKey(
                blank=True,
                help_text="The User who last edited this %(class)",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_updated_by",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Last edit User",
            ),
        ),
        migrations.AddField(
            model_name="session",
            name="edit_by",
            field=models.ForeignKey(
                blank=True,
                help_text="The User who last edited this %(class)",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_updated_by",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Last edit User",
            ),
        ),
        migrations.AddField(
            model_name="trainer",
            name="edit_by",
            field=models.ForeignKey(
                blank=True,
                help_text="The User who last edited this %(class)",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_updated_by",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Last edit User",
            ),
        ),
        migrations.AddField(
            model_name="trainer",
            name="is_trashed",
            field=models.BooleanField(
                default=False, help_text="Is the object trashed", verbose_name="Trashed"
            ),
        ),
        migrations.AlterField(
            model_name="approvalstate",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                help_text="The User who has created this %(class)",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_created_by",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Creation User",
            ),
        ),
        migrations.AlterField(
            model_name="approvalstate",
            name="creation_date",
            field=models.DateTimeField(
                auto_now_add=True,
                help_text="Date and Time of %(class)'s creation",
                verbose_name="Creation Date and Time",
            ),
        ),
        migrations.AlterField(
            model_name="approvalstate",
            name="description",
            field=models.TextField(
                blank=True,
                default="",
                help_text="%(class) description",
                verbose_name="Description",
            ),
        ),
        migrations.AlterField(
            model_name="approvalstate",
            name="edit_date",
            field=models.DateTimeField(
                auto_now=True,
                help_text="Date and Time of object's last edit",
                verbose_name="Last edit Date and Time",
            ),
        ),
        migrations.AlterField(
            model_name="enrollment",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                help_text="The User who has created this %(class)",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_created_by",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Creation User",
            ),
        ),
        migrations.AlterField(
            model_name="enrollment",
            name="creation_date",
            field=models.DateTimeField(
                auto_now_add=True,
                help_text="Date and Time of %(class)'s creation",
                verbose_name="Creation Date and Time",
            ),
        ),
        migrations.AlterField(
            model_name="enrollment",
            name="edit_date",
            field=models.DateTimeField(
                auto_now=True,
                help_text="Date and Time of object's last edit",
                verbose_name="Last edit Date and Time",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                help_text="The User who has created this %(class)",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_created_by",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Creation User",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="creation_date",
            field=models.DateTimeField(
                auto_now_add=True,
                help_text="Date and Time of %(class)'s creation",
                verbose_name="Creation Date and Time",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="edit_date",
            field=models.DateTimeField(
                auto_now=True,
                help_text="Date and Time of object's last edit",
                verbose_name="Last edit Date and Time",
            ),
        ),
        migrations.AlterField(
            model_name="presence",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                help_text="The User who has created this %(class)",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_created_by",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Creation User",
            ),
        ),
        migrations.AlterField(
            model_name="presence",
            name="creation_date",
            field=models.DateTimeField(
                auto_now_add=True,
                help_text="Date and Time of %(class)'s creation",
                verbose_name="Creation Date and Time",
            ),
        ),
        migrations.AlterField(
            model_name="presence",
            name="edit_date",
            field=models.DateTimeField(
                auto_now=True,
                help_text="Date and Time of object's last edit",
                verbose_name="Last edit Date and Time",
            ),
        ),
        migrations.AlterField(
            model_name="session",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                help_text="The User who has created this %(class)",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_created_by",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Creation User",
            ),
        ),
        migrations.AlterField(
            model_name="session",
            name="creation_date",
            field=models.DateTimeField(
                auto_now_add=True,
                help_text="Date and Time of %(class)'s creation",
                verbose_name="Creation Date and Time",
            ),
        ),
        migrations.AlterField(
            model_name="session",
            name="edit_date",
            field=models.DateTimeField(
                auto_now=True,
                help_text="Date and Time of object's last edit",
                verbose_name="Last edit Date and Time",
            ),
        ),
        migrations.AlterField(
            model_name="trainer",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                help_text="The User who has created this %(class)",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_created_by",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Creation User",
            ),
        ),
        migrations.AlterField(
            model_name="trainer",
            name="creation_date",
            field=models.DateTimeField(
                auto_now_add=True,
                help_text="Date and Time of %(class)'s creation",
                verbose_name="Creation Date and Time",
            ),
        ),
        migrations.AlterField(
            model_name="trainer",
            name="edit_date",
            field=models.DateTimeField(
                auto_now=True,
                help_text="Date and Time of object's last edit",
                verbose_name="Last edit Date and Time",
            ),
        ),
    ]
