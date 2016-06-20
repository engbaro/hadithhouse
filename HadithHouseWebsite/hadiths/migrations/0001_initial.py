# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 08:12
from __future__ import unicode_literals

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
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('simple_title', models.CharField(default='', max_length=128)),
                ('brief_desc', models.CharField(blank=True, max_length=256, null=True)),
                ('simple_brief_desc', models.CharField(blank=True, max_length=256, null=True)),
                ('pub_year', models.SmallIntegerField(blank=True, db_index=True, null=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books_added', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'books',
                'default_permissions': ('add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='BookChapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('simple_title', models.CharField(max_length=128)),
                ('number', models.SmallIntegerField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookchapters_added', to=settings.AUTH_USER_MODEL)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='hadiths.Book')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'bookchapters',
                'default_permissions': ('add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='BookSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('simple_title', models.CharField(max_length=128)),
                ('number', models.SmallIntegerField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='booksections_added', to=settings.AUTH_USER_MODEL)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='hadiths.Book')),
                ('chapter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='hadiths.BookChapter')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'booksections',
                'default_permissions': ('add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='BookVolume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('simple_title', models.CharField(max_length=128)),
                ('number', models.SmallIntegerField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookvolumes_added', to=settings.AUTH_USER_MODEL)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='volumes', to='hadiths.Book')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'bookvolumes',
                'default_permissions': ('add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='Chain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chains_added', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'chains',
                'default_permissions': ('add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='ChainPersonRel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.SmallIntegerField()),
                ('chain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_rels', to='hadiths.Chain')),
            ],
            options={
                'db_table': 'chains_persons',
                'default_permissions': ('add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='FbUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb_id', models.BigIntegerField(unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fb_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'fb_users',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Hadith',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(db_index=True)),
                ('simple_text', models.TextField(db_index=True, default='')),
                ('number', models.SmallIntegerField(blank=True, db_index=True, null=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hadiths_added', to=settings.AUTH_USER_MODEL)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='hadiths', to='hadiths.Book')),
                ('chapter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='hadiths', to='hadiths.BookChapter')),
            ],
            options={
                'db_table': 'hadiths',
                'default_permissions': ('add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='HadithTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('simple_name', models.CharField(default='', max_length=32)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hadithtags_added', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'hadithtags',
                'default_permissions': ('add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='HadithTagRel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('hadith', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag_rels', to='hadiths.Hadith')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='hadith_rels', to='hadiths.HadithTag')),
            ],
            options={
                'db_table': 'hadiths_hadithtags',
                'default_permissions': ('add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=16, null=True)),
                ('display_name', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('simple_display_name', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('full_name', models.CharField(max_length=255, unique=True)),
                ('simple_full_name', models.CharField(default='', max_length=255)),
                ('brief_desc', models.CharField(blank=True, max_length=512, null=True)),
                ('simple_brief_desc', models.CharField(blank=True, max_length=512, null=True)),
                ('birth_year', models.SmallIntegerField(blank=True, null=True)),
                ('birth_month', models.SmallIntegerField(blank=True, null=True)),
                ('birth_day', models.SmallIntegerField(blank=True, null=True)),
                ('death_year', models.SmallIntegerField(blank=True, null=True)),
                ('death_month', models.SmallIntegerField(blank=True, null=True)),
                ('death_day', models.SmallIntegerField(blank=True, null=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='persons_added', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'persons',
                'default_permissions': ('add', 'change', 'delete'),
            },
        ),
        migrations.AddField(
            model_name='hadith',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='hadiths', to='hadiths.Person'),
        ),
        migrations.AddField(
            model_name='hadith',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='hadiths', to='hadiths.BookSection'),
        ),
        migrations.AddField(
            model_name='hadith',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hadith',
            name='volume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='hadiths', to='hadiths.BookVolume'),
        ),
        migrations.AddField(
            model_name='chainpersonrel',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='chain_rels', to='hadiths.Person'),
        ),
        migrations.AddField(
            model_name='chain',
            name='hadith',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chains', to='hadiths.Hadith'),
        ),
        migrations.AddField(
            model_name='chain',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookchapter',
            name='volume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='hadiths.BookVolume'),
        ),
        migrations.AlterUniqueTogether(
            name='hadithtagrel',
            unique_together=set([('hadith', 'tag')]),
        ),
        migrations.AlterUniqueTogether(
            name='chainpersonrel',
            unique_together=set([('chain', 'person')]),
        ),
    ]
