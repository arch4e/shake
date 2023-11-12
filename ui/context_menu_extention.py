# -*- coding: utf-8 -*-
import bpy


class ShaKe_MT_move_shape_key_below_selected(bpy.types.Menu):
    bl_idname = 'OBJECT_MT_ShaKe_move_shapekey_below_selected'
    bl_label  = 'Move Shape Key'

    def draw(self, context):
        layout     = self.layout
        shape_keys = context.active_object.data.shape_keys
        if hasattr(shape_keys, 'key_blocks'):
            for name, _ in list(shape_keys.key_blocks.items()):
                layout.operator('shake.move_shapekey_below_selected', text=name).target = name


def ShaKe_MT_shape_keys_extended_menu(self, context):
    layout = self.layout
    layout.separator()
    layout.menu('OBJECT_MT_ShaKe_move_shapekey_below_selected', text='Move Shape Key')
    layout.operator('shake.align_by_prefix', text='Align by Prefix')

