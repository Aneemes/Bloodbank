from django.db import migrations, models
import django.core.validators

class Migration(migrations.Migration):

    dependencies = [
        ('BloodBank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/uploads')),
                ('name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2)])),
                ('expert', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
