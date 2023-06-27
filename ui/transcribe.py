# -*- coding: utf-8 -*-
import bpy

from .common import BasePanel
from ..operator.transcribe import destination_objects, selected_shape_keys


class TranscribePanel(BasePanel, bpy.types.Panel):
    bl_idname  = 'VIEW3D_PT_shaku_transcribe'
    bl_label   = 'Transcribe Shape Keys'
    bl_options = {'HEADER_LAYOUT_EXPAND'}

    def draw(self, context):
        # Objects with names containing non-ASCII characters are garbled in EnumProperty
        USING_SUPPORTED_LANG = not (
            bpy.context.preferences.view.language != 'en_US' # noqa: W503
            and (bpy.context.preferences.view.use_translate_new_dataname is True)
        )

        col  = self.layout.column()

        # Mode Selector
        if USING_SUPPORTED_LANG:
            col.prop(context.scene.shaku_transcribe, 'source_mode_single_object', text='Source Mode: Single Object')
            col.separator(factor=0.5)
        else:
            col.label(text='Non-ASCII name is not supported', icon='ERROR')

        # Source Object Selector
        if context.scene.shaku_transcribe.source_mode_single_object:
            col.label(text='src: Mesh Object', icon='OBJECT_DATA')
            col.prop(context.scene.shaku_transcribe, 'source', text='')

        # Target Shape Key Selector
        col.separator(factor=0.5)
        col.label(text='tgt: Shape Keys', icon='SHAPEKEY_DATA')
        tbox = col.box().column(align=True)
        if context.scene.shaku_transcribe.source_mode_single_object:
            shape_keys = bpy.data.objects[context.scene.shaku_transcribe.source].data.shape_keys
            if type(shape_keys) == bpy.types.Key:
                for (shape_key_name, _) in shape_keys.key_blocks.items():
                    row = tbox.row()
                    row.alignment = 'LEFT'
                    row.operator('shaku.select_shape_keys',
                                 icon='CHECKBOX_HLT' if shape_key_name in selected_shape_keys else 'CHECKBOX_DEHLT',
                                 text=f'{shape_key_name}',
                                 emboss=False).shape_key_name = shape_key_name
            else:
                tbox.label(text='N/A')
        else:
            shape_keys = get_all_shape_key_name()
            if len(shape_keys) <= 0:
                tbox.label(text='N/A')
            else:
                for shape_key_name in shape_keys:
                    row = tbox.row()
                    row.alignment = 'LEFT'
                    row.operator('shaku.select_shape_keys',
                                 icon='CHECKBOX_HLT' if shape_key_name in selected_shape_keys else 'CHECKBOX_DEHLT',
                                 text=f'{shape_key_name}',
                                 emboss=False).shape_key_name = shape_key_name

        # Separator
        col.separator(factor=0.5)
        sep = col.row(align=True)
        sep.alignment = 'CENTER'
        sep.label(icon='TRIA_DOWN')

        # Destination Object Selector
        col.separator(factor=0.5)
        col.label(text='dst: Mesh Objects', icon='OBJECT_DATA')
        col.prop(context.scene.shaku_transcribe, 'filter_collection', text='Filter:')
        dbox = col.box().column(align=True)
        object_list = []
        if context.scene.shaku_transcribe.filter_collection != 'ALL':
            object_list = [obj.name for (_, obj) in bpy.data.collections[context.scene.shaku_transcribe.filter_collection].objects.items() if obj.type == 'MESH']
        else:
            object_list = [obj.name for (_, obj) in bpy.data.objects.items() if obj.type == 'MESH']

        for object_name in object_list:
            row = dbox.row()
            row.alignment = 'LEFT'
            row.operator('shaku.select_destination_objects',
                         icon='CHECKBOX_HLT' if object_name in destination_objects else 'CHECKBOX_DEHLT',
                         text=f'{object_name}',
                         emboss=False).object_name = object_name

        # Transcribe Button
        col.separator(factor=1.5)
        btn = col.row(align=True)
        btn.operator('shaku.transcribe_shape_keys', icon='DUPLICATE', text='transcribe')


def get_all_shape_key_name():
    shape_keys = []
    for _object in [obj for (_, obj) in bpy.data.objects.items() if obj.type == 'MESH']:
        if _object.data.shape_keys is not None:
            shape_keys.extend(_object.data.shape_keys.key_blocks.keys())

    shape_keys = list(set(shape_keys))
    shape_keys.sort()

    return shape_keys

