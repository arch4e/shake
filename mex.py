# -*- coding: utf-8 -*-
import bpy
import re

bl_info = {
    "name"    : "MEX",
    "category": "3D View",
    "location": "",
    "version" : (0,2,0),
    "blender" : (3,0,0),
    "author"  : "arch4e"
}

#
# Operator
#
class OpsShapeKeyMoveToSelect(bpy.types.Operator):
    bl_idname = 'mex.sk_move_to_select'
    bl_label  = 'Move Shape Key: to Select'

    target: bpy.props.StringProperty()

    # move selected sk below target
    def execute(self, context):
        key_blocks = context.active_object.data.shape_keys.key_blocks
        index_diff = context.object.active_shape_key_index - key_blocks.find(self.target)
        if index_diff > 1:
            type = 'UP'
        elif index_diff < -1:
            type = 'DOWN'
            index_diff -= 1 # magic
        else:
            return {'FINISHED'}

        index_diff = abs(index_diff)
        while index_diff > 1:
            bpy.ops.object.shape_key_move(type=type)
            index_diff -= 1

        return {'FINISHED'}

class OpsShapeKeyBindWithPrefix(bpy.types.Operator):
    bl_idname = 'mex.sk_bind_with_prefix'
    bl_label  = 'Bind With Prefix'

    def execute(self, context):
        bind_shape_key(context)        

        return {'FINISHED'}

def bind_shape_key(context):
    key_blocks = context.active_object.data.shape_keys.key_blocks
    prefix_end = {}

    for key_name in [shape_key.name for shape_key in key_blocks]:
        prefix = re.split(r'\.|_', key_name, 1)[0] # <prefix>_<shape key name>
        # update value if prefix is new or contiguous
        if not prefix in prefix_end.keys() \
           or prefix == re.split(r'\.|_', key_blocks[key_blocks.find(key_name) - 1].name, 1)[0]:
            prefix_end[prefix] = key_blocks.find(key_name)

        while key_blocks.find(key_name) >= (prefix_end[prefix] + 2):
            bpy.context.object.active_shape_key_index = key_blocks.find(key_name)
            bpy.ops.object.shape_key_move(type='UP')
            # update prefix_end when the move is complete
            if key_blocks.find(key_name) <= (prefix_end[prefix] + 1):
                # update all prefix_end after the target prefix
                for p in prefix_end.keys():
                    if prefix_end[p] >= prefix_end[prefix]:
                        prefix_end[p] += 1

#
# Menu
#
class MenuShapeKeyMoveToSelect(bpy.types.Menu):
    bl_idname = 'OBJECT_MT_mex_sk_move_to_select'
    bl_label  = 'Move Shape Key: to Select'

    def draw(self, context):
        layout     = self.layout
        shape_keys = context.active_object.data.shape_keys
        if hasattr(shape_keys, 'key_blocks'):
            for name, _ in list(shape_keys.key_blocks.items()):
                layout.operator('mex.sk_move_to_select', text=name).target = name

def sk_exmenu(self, context):
    layout = self.layout
    layout.separator()
    layout.menu('OBJECT_MT_mex_sk_move_to_select', text='Move: to Select')
    layout.operator('mex.sk_bind_with_prefix', text='Bind With Prefix')

classes = [
    MenuShapeKeyMoveToSelect,
    OpsShapeKeyMoveToSelect,
    OpsShapeKeyBindWithPrefix
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.MESH_MT_shape_key_context_menu.append(sk_exmenu)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.MESH_MT_shape_key_context_menu.remove(sk_exmenu)

if __name__ == '__main__':
    register()

