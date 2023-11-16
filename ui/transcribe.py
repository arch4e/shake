# -*- coding: utf-8 -*-
import bpy

from .common import BasePanel
from .selector import draw_selected_shape_key_list
from ..operator.transcribe import destination_objects


class ShaKe_PT_transcribe(BasePanel, bpy.types.Panel):
    bl_idname  = 'VIEW3D_PT_shake_transcribe'
    bl_label   = 'Transcribe Shape Keys'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        col = self.layout.column()
        col.enabled = context.object.mode != 'EDIT'

        # Selected Shape Keys
        draw_selected_shape_key_list(col)

        # Separator
        col.separator(factor=0.5)
        sep = col.row(align=True)
        sep.alignment = 'CENTER'
        sep.label(icon='TRIA_DOWN')

        # Destination Object Selector
        col.separator(factor=0.5)
        col.label(text='dst: Mesh Objects', icon='OBJECT_DATA')
        col.prop(context.scene.shake_transcribe, 'filter_collection', text='Filter:')
        dbox = col.box().column(align=True)
        object_list = []
        if context.scene.shake_transcribe.filter_collection != 'ALL':
            object_list = [obj.name for (_, obj) in bpy.data.collections[context.scene.shake_transcribe.filter_collection].objects.items() if obj.type == 'MESH']
        else:
            object_list = [obj.name for (_, obj) in bpy.data.objects.items() if obj.type == 'MESH']

        for object_name in object_list:
            row = dbox.row()
            row.alignment = 'LEFT'
            row.operator('shake.select_destination_objects',
                         icon='CHECKBOX_HLT' if object_name in destination_objects else 'CHECKBOX_DEHLT',
                         text=f'{object_name}',
                         emboss=False).object_name = object_name

        # Transcribe Button
        col.separator(factor=1.5)
        btn = col.row(align=True)
        btn.operator('shake.transcribe_shape_keys', icon='DUPLICATE', text='transcribe')


def get_all_shape_key_name():
    shape_keys = []
    for _object in [obj for (_, obj) in bpy.data.objects.items() if obj.type == 'MESH']:
        if _object.data.shape_keys is not None:
            shape_keys.extend(_object.data.shape_keys.key_blocks.keys())

    shape_keys = list(set(shape_keys))
    shape_keys.sort()

    return shape_keys

