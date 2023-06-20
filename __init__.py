# -*- coding: utf-8 -*-
import bpy

from .operator.context_menu_extention import ShapeKeyMoveBelowSelect, ShapeKeyAlignByPrefix
from .ui.context_menu_extention import MenuShapeKeyMoveBelowSelect, extended_menu

bl_info = {
    'name'    : 'ShaKU',
    'category': '3D View',
    'location': '',
    'version' : (1,0,0),
    'blender' : (3,0,0),
    'author'  : 'arch4e'
}

classes = [
    MenuShapeKeyMoveBelowSelect,
    ShapeKeyMoveBelowSelect,
    ShapeKeyAlignByPrefix
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.MESH_MT_shape_key_context_menu.append(extended_menu)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.MESH_MT_shape_key_context_menu.remove(extended_menu)

if __name__ == '__main__':
    register()

