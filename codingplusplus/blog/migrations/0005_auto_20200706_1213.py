# Generated by Django 3.0.7 on 2020-07-06 06:43

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("taggit", "0003_taggeditem_add_unique_index"),
        ("blog", "0004_auto_20200702_1756"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogentrypage",
            name="CoverImage",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "cover_image",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "Image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        blank=True, null=True, required=False
                                    ),
                                ),
                                (
                                    "ImageViaUrl",
                                    wagtail.core.blocks.URLBlock(
                                        blank=True, null=True, required=False
                                    ),
                                ),
                                (
                                    "ImageOverride",
                                    wagtail.core.blocks.BooleanBlock(
                                        blank=True,
                                        help_text="Use Image Via url Instead of Image uploaded",
                                        null=True,
                                        required=False,
                                    ),
                                ),
                                (
                                    "AltText",
                                    wagtail.core.blocks.TextBlock(
                                        blank=True, null=True, required=False
                                    ),
                                ),
                                (
                                    "Position",
                                    wagtail.core.blocks.ChoiceBlock(
                                        blank=True,
                                        choices=[
                                            ("center", "center"),
                                            ("top", "top"),
                                            ("left", "left"),
                                            ("right", "right"),
                                        ],
                                        help_text="No Effect On Cover Image",
                                        null=True,
                                        required=False,
                                    ),
                                ),
                                (
                                    "ClearFix",
                                    wagtail.core.blocks.BooleanBlock(
                                        blank=True,
                                        help_text="Pushes content Down instead of wraping around it",
                                        null=True,
                                        required=False,
                                    ),
                                ),
                            ],
                            block_counts={
                                "AltText": {"max_num": 1},
                                "Image": {"max_num": 1},
                                "ImageViaUrl": {"max_num": 1},
                                "position": {"max_num": 1},
                            },
                        ),
                    )
                ],
                verbose_name="Cover Image",
            ),
        ),
        migrations.AlterField(
            model_name="blogentrypage",
            name="body",
            field=wagtail.core.fields.StreamField(
                [
                    ("Title", wagtail.core.blocks.CharBlock(blank=False, null=True)),
                    (
                        "body",
                        wagtail.core.blocks.RichTextBlock(
                            blank=True, closed=True, null=True
                        ),
                    ),
                    (
                        "image",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "Image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        blank=True, null=True, required=False
                                    ),
                                ),
                                (
                                    "ImageViaUrl",
                                    wagtail.core.blocks.URLBlock(
                                        blank=True, null=True, required=False
                                    ),
                                ),
                                (
                                    "ImageOverride",
                                    wagtail.core.blocks.BooleanBlock(
                                        blank=True,
                                        help_text="Use Image Via url Instead of Image uploaded",
                                        null=True,
                                        required=False,
                                    ),
                                ),
                                (
                                    "AltText",
                                    wagtail.core.blocks.TextBlock(
                                        blank=True, null=True, required=False
                                    ),
                                ),
                                (
                                    "Position",
                                    wagtail.core.blocks.ChoiceBlock(
                                        blank=True,
                                        choices=[
                                            ("center", "center"),
                                            ("top", "top"),
                                            ("left", "left"),
                                            ("right", "right"),
                                        ],
                                        help_text="No Effect On Cover Image",
                                        null=True,
                                        required=False,
                                    ),
                                ),
                                (
                                    "ClearFix",
                                    wagtail.core.blocks.BooleanBlock(
                                        blank=True,
                                        help_text="Pushes content Down instead of wraping around it",
                                        null=True,
                                        required=False,
                                    ),
                                ),
                            ],
                            blank=True,
                            max_num=1,
                            min_num=1,
                            null=True,
                        ),
                    ),
                ]
            ),
        ),
        migrations.CreateModel(
            name="BlogEntryPageTag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "content_object",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tagged_items",
                        to="blog.BlogEntryPage",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="blog_blogentrypagetag_items",
                        to="taggit.Tag",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.AddField(
            model_name="blogentrypage",
            name="tags",
            field=modelcluster.contrib.taggit.ClusterTaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="blog.BlogEntryPageTag",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
