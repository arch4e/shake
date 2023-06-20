import bpy

class MenuShapeKeyMoveBelowSelect(bpy.types.Menu):
    bl_idname = 'OBJECT_MT_shake_tools_move_below_selected'
    bl_label  = 'Move Shape Key'

    def draw(self, context):
        layout     = self.layout
        shape_keys = context.active_object.data.shape_keys
        if hasattr(shape_keys, 'key_blocks'):
            for name, _ in list(shape_keys.key_blocks.items()):
                layout.operator('shake_tools.move_below_selected', text=name).target = name

def extended_menu(self, context):
    layout = self.layout
    layout.separator()
    layout.menu('OBJECT_MT_shake_tools_move_below_selected', text='Move Shape Key')
    layout.operator('shake_tools.align_by_prefix', text='Align by Prefix')

