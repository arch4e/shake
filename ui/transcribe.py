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

        # Source Object Selector
        col.label(text='src: Mesh Object', icon='OBJECT_DATA')
        col.prop(context.scene.shaku_transcribe, 'source', text='')

        # Target Shape Key Selector
        col.separator(factor=0.5)
        col.label(text='tgt: Shape Keys', icon='SHAPEKEY_DATA')
        tbox = col.box().column(align=True)
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

