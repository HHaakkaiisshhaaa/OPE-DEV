# Generated by Django 2.2.1 on 2019-05-13 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=30)),
                ('descricao_produto', models.CharField(max_length=50)),
                ('preco_compra', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantidade_produto', models.IntegerField()),
            ],
        ),
    ]
