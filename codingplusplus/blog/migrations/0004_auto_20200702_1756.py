# Generated by Django 3.0.7 on 2020-07-02 12:26

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_delete_navbar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentrypage',
            name='CoverImage',
            field=wagtail.core.fields.StreamField([('cover_image', wagtail.core.blocks.StructBlock([('Image', wagtail.images.blocks.ImageChooserBlock(blank=True, null=True, required=False)), ('ImageViaUrl', wagtail.core.blocks.URLBlock(blank=True, null=True, required=False)), ('ImageOverride', wagtail.core.blocks.BooleanBlock(blank=True, help_text='Use Image Via url Instead of Image uploaded', null=True, required=False)), ('AltText', wagtail.core.blocks.TextBlock(blank=True, null=True, required=False)), ('Position', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('center', 'center'), ('bottom', 'bottom'), ('top', 'top'), ('left', 'left'), ('left-bottom', 'left bottom'), ('left-top', 'left top'), ('right', 'right'), ('right-top', 'right top'), ('right-bottom', 'right bottom')], help_text='No Effect On Cover Image', null=True, required=False))], block_counts={'AltText': {'max_num': 1}, 'Image': {'max_num': 1}, 'ImageViaUrl': {'max_num': 1}, 'position': {'max_num': 1}}))], blank=True),
        ),
        migrations.AlterField(
            model_name='blogentrypage',
            name='body',
            field=wagtail.core.fields.StreamField([('Title', wagtail.core.blocks.CharBlock(blank=False, null=True)), ('body', wagtail.core.blocks.RichTextBlock(blank=True, null=True)), ('image', wagtail.core.blocks.StructBlock([('Image', wagtail.images.blocks.ImageChooserBlock(blank=True, null=True, required=False)), ('ImageViaUrl', wagtail.core.blocks.URLBlock(blank=True, null=True, required=False)), ('ImageOverride', wagtail.core.blocks.BooleanBlock(blank=True, help_text='Use Image Via url Instead of Image uploaded', null=True, required=False)), ('AltText', wagtail.core.blocks.TextBlock(blank=True, null=True, required=False)), ('Position', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('center', 'center'), ('bottom', 'bottom'), ('top', 'top'), ('left', 'left'), ('left-bottom', 'left bottom'), ('left-top', 'left top'), ('right', 'right'), ('right-top', 'right top'), ('right-bottom', 'right bottom')], help_text='No Effect On Cover Image', null=True, required=False))], blank=True, max_num=1, min_num=1, null=True))]),
        ),
        migrations.AlterField(
            model_name='blogentrypage',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
