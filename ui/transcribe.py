import bpy

from .common import BasePanel
from ..operator.transcribe import destination_objects, target_shape_keys


class TranscribePanel(BasePanel, bpy.types.Panel):
    bl_idname  = 'VIEW3D_PT_shaku_transcribe'
    bl_label   = 'Transcribe Shape Keys'
    bl_options = {'HEADER_LAYOUT_EXPAND'}

    def draw(self, context):
        shape_keys = bpy.data.objects[context.scene.shaku_transcribe.source].data.shape_keys
        col  = self.layout.column()

        # Mode Selector
        col.prop(context.scene.shaku_transcribe, 'select_mode_all_sk', text='Select Mode: ALL Shape Keys')
        col.label(text='!!! This option is high load !!!')
        col.separator(factor=0.5)

        # Source Object Selector
        if not context.scene.shaku_transcribe.select_mode_all_sk:
            col.label(text='src: Mesh Object', icon='OBJECT_DATA')
            col.prop(context.scene.shaku_transcribe, 'source', text='')

        # Target Shape Key Selector
        col.separator(factor=0.5)
        col.label(text='tgt: Shape Keys', icon='SHAPEKEY_DATA')
        tbox = col.box().column(align=True)
        if context.scene.shaku_transcribe.select_mode_all_sk:
            shape_keys = get_all_shape_key_name()
            if len(shape_keys) <= 0:
                tbox.label(text='N/A')
            else:
                for shape_key_name in shape_keys:
                    row = tbox.row()
                    row.alignment = 'LEFT'
                    row.operator('shaku.select_shape_keys',
                                 icon='CHECKBOX_HLT' if shape_key_name in target_shape_keys else 'CHECKBOX_DEHLT',
                                 text=f'{shape_key_name}',
                                 emboss=False).shape_key_name = shape_key_name
        else:
            if type(shape_keys) == bpy.types.Key:
                for (shape_key_name, _) in shape_keys.key_blocks.items():
                    row = tbox.row()
                    row.alignment = 'LEFT'
                    row.operator('shaku.select_shape_keys',
                                 icon='CHECKBOX_HLT' if shape_key_name in target_shape_keys else 'CHECKBOX_DEHLT',
                                 text=f'{shape_key_name}',
                                 emboss=False).shape_key_name = shape_key_name
            else:
                tbox.label(text='N/A')

        # Separator
        col.separator(factor=0.5)
        sep = col.row(align=True)
        sep.alignment = 'CENTER'
        sep.label(icon='TRIA_DOWN')

        # Destination Object Selector
        col.separator(factor=0.5)
        col.label(text='dst: Mesh Objects', icon='OBJECT_DATA')
        dbox = col.box().column(align=True)
        for object_name in [obj.name for (_, obj) in bpy.data.objects.items() if obj.type == 'MESH']:
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
        if not _object.data.shape_keys is None:
            shape_keys.extend(_object.data.shape_keys.key_blocks.keys())

    shape_keys = list(set(shape_keys))
    shape_keys.sort()

    return shape_keys

