# -*- coding: utf-8 -*-
import bpy

from .common import BasePanel


class ShaKe_PT_create_shape_keys_from_csv(BasePanel, bpy.types.Panel):
    bl_idname = 'VIEW3D_PT_ShaKe_create_shape_keys_from_csv'
    bl_label  = 'Create Shape Keys from CSV'

    file_name: bpy.props.StringProperty

    @classmethod
    def poll(cls, context):
        return context.object

    def draw(self, context):
        col = self.layout.column()
        col.enabled = context.object.mode != 'EDIT' and len(bpy.data.texts) > 0

        col.prop(context.scene.shake_create_shape_keys_csv, 'csv_file_name', icon='FILE', text='')
        col.operator('shake.create_shape_keys_from_csv', text='create shape key from csv')
