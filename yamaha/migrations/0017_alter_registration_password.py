from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yamaha', '0016_variants_accessed_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]