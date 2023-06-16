# Generated by Django 4.2.1 on 2023-06-16 17:08

import asso.core.utils
from decimal import Decimal
from django.db import migrations, models
import djmoney.models.fields
import relativedeltafield.fields


class Migration(migrations.Migration):
    dependencies = [
        (
            "membership",
            "0014_remove_member_first_name_remove_member_last_name_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="membershipperiod",
            name="duration",
            field=relativedeltafield.fields.RelativeDeltaField(
                default=asso.core.utils.yearly_duration,
                help_text="How long is the Membership Period",
                verbose_name="Duration",
            ),
        ),
        migrations.AlterField(
            model_name="membershipperiod",
            name="price",
            field=djmoney.models.fields.MoneyField(
                decimal_places=2,
                default=Decimal("0.0"),
                default_currency="EUR",
                help_text="The default price to pay for this Period Membership",
                max_digits=10,
                verbose_name="Price",
            ),
        ),
        migrations.AlterField(
            model_name="membershipperiod",
            name="start_date",
            field=models.DateField(
                default=asso.core.utils.year_first_day,
                help_text="It is the day the Membership starts",
                verbose_name="Start Date",
            ),
        ),
    ]