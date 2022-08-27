from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('weather', models.IntegerField(choices=[('0', '#맑음'), ('1', '#흐림'), ('2', '#비'), ('3', '#눈'), ('4', '#바람')], default=0)),
                ('temp', models.CharField(max_length=5)),
                ('finedust', models.IntegerField(choices=[('0', '#좋음'), ('1', '#조금좋음'), ('2', '#보통'), ('3', '#조금나쁨'), ('4', '#나쁨')], default=0)),
                ('tmi', models.TextField(blank=True, null=True)),
                ('liked', models.IntegerField(blank=True, null=True)),
                ('scrap', models.IntegerField(blank=True, null=True)),
                ('wear_tag1', models.CharField(max_length=10)),
                ('wear_tag2', models.CharField(blank=True, max_length=10, null=True)),
                ('wear_tag3', models.CharField(blank=True, max_length=10, null=True)),
                ('weather_tag1', models.CharField(max_length=10)),
                ('weather_tag2', models.CharField(blank=True, max_length=10, null=True)),
                ('weather_tag3', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30)),
                ('user_image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('intro', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Scrap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scrap_post', to='post.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scrap_user', to='post.user')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.user'),
        ),
    ]
