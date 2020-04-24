# Generated by Django 3.0.5 on 2020-04-24 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20200424_0808'),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('line_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='carts.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='menu.product')),
            ],
        ),
    ]