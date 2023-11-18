# -*- coding: utf-8 -*-
import bpy
import re


class ShaKe_OT_create_shape_keys_from_csv(bpy.types.Operator):
    bl_idname = 'shake.create_shape_keys_from_csv'
    bl_label  = 'Create Shape Keys from CSV'

    def execute(self, context):
        text_file_name = context.scene.shake_create_shape_keys_csv.csv_file_name
        if text_file_name in bpy.data.texts.items():
            return {'CANCELED'}

        # read file content
        content = bpy.data.texts[text_file_name].as_string()
        shape_key_names = re.split(r'\n|\\r\\n|,', content)

        # create basis key
        if context.active_object.data.shape_keys is None:
            context.active_object.shape_key_add(name='Basis', from_mix=False)

        # drop empty, exist keys and duplicated keys
        shape_key_names = list(dict.fromkeys(shape_key_names))
        exist_shape_key_names = context.active_object.data.shape_keys.key_blocks.keys()
        shape_key_names = list(filter(lambda x: ((x != '') and (not (x in exist_shape_key_names))), shape_key_names))

        # add shape keys
        for _shape_key_name in shape_key_names:
            context.active_object.shape_key_add(name=_shape_key_name, from_mix=False)

        return {'FINISHED'}
