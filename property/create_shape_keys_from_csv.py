# -*- coding: utf-8 -*-
import bpy


def generate_text_file_list(self, context):
    text_files = [(text.name, text.name, '') for text in bpy.data.texts]
    return text_files


class ShaKe_PG_create_shape_keys_from_csv(bpy.types.PropertyGroup):
    csv_file_name: bpy.props.EnumProperty(
        name='Selected Text File', # noqa: F722
        items=generate_text_file_list
    )
