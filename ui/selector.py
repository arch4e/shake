# -*- coding: utf-8 -*-
import bpy

from .common import BasePanel
from ..operator.selector import selected_shape_keys


class ShaKe_PT_shape_keys_selector(BasePanel, bpy.types.Panel):
    bl_idname = 'VIEW3D_PT_ShaKe_shape_keys_selector'
    bl_label  = 'Shape Keys Selector'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.object

    def draw(self, context):
        # Objects with names containing non-ASCII characters are garbled in EnumProperty
        USING_SUPPORTED_LANG = not (bpy.context.preferences.view.language != 'en_US'
                                    and (bpy.context.preferences.view.use_translate_new_dataname is True)) # noqa: W503

        col = self.layout.column()
        col.enabled = context.object.mode != 'EDIT'

        # Mode Selector
        if USING_SUPPORTED_LANG:
            col.prop(context.scene.shake_transcribe, 'source_mode_single_object', text='Source Mode: Single Object')
            col.separator(factor=0.5)
        else:
            col.label(text='Non-ASCII name is not supported', icon='ERROR')

        # Source Object Selector
        if context.scene.shake_transcribe.source_mode_single_object:
            col.label(text='src: Mesh Object', icon='OBJECT_DATA')
            col.prop(context.scene.shake_transcribe, 'source', text='')

        # Shape Key List
        box = col.box().column(align=True)
        shape_keys = []
        if context.scene.shake_transcribe.source_mode_single_object:
            _shape_keys = bpy.data.objects[context.scene.shake_transcribe.source].data.shape_keys
            if type(_shape_keys) == bpy.types.Key:
                shape_keys = [x for (x, _) in _shape_keys.key_blocks.items()]
        else:
            shape_keys = get_all_shape_key_name()

        if len(shape_keys) > 0:
            for _shape_key in shape_keys:
                row = box.row()
                row.alignment = 'LEFT'
                row.operator('shake.select_shape_key',
                             icon='CHECKBOX_HLT' if _shape_key in selected_shape_keys else 'CHECKBOX_DEHLT',
                             text=f'{_shape_key}',
                             emboss=False).shape_key_name = _shape_key
        else:
            box.label(text='N/A')


def draw_selected_shape_key_list(layout):
    layout.label(text='Selected Shape Keys:', icon='SHAPEKEY_DATA')
    box = layout.box().column(align=True)
    for _shape_key in selected_shape_keys:
        box.label(text=f'{_shape_key}')


def get_all_shape_key_name():
    shape_keys = []
    for _object in [obj for (_, obj) in bpy.data.objects.items() if obj.type == 'MESH']:
        if _object.data.shape_keys is not None:
            shape_keys.extend(_object.data.shape_keys.key_blocks.keys())

    shape_keys = list(set(shape_keys))
    shape_keys.sort()

    return shape_keys
