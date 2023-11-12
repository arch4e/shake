# -*- coding: utf-8 -*-
import bpy

selected_shape_keys = []


class ShaKe_OT_select_shape_key(bpy.types.Operator):
    bl_idname = 'shake.select_shape_key'
    bl_label  = 'Select Shape Key'

    shape_key_name: bpy.props.StringProperty()

    def execute(self, context):
        if self.shape_key_name in selected_shape_keys:
            selected_shape_keys.remove(self.shape_key_name)
        else:
            selected_shape_keys.append(self.shape_key_name)

        return { 'FINISHED' }
