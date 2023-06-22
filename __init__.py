# -*- coding: utf-8 -*-
import bpy

from .operator.context_menu_extention import ShapeKeyMoveBelowSelect, ShapeKeyAlignByPrefix
from .operator.transcribe import SelectDestination, SelectShapeKeys, TranscribeShapeKeys
from .property.transcribe import TranscribeProps
from .ui.context_menu_extention import MenuShapeKeyMoveBelowSelect, extended_menu
from .ui.transcribe import TranscribePanel
from .util.props_register import register as props_register, unregister as props_unregister

bl_info = {
    'name'    : 'ShaKU',
    'category': '3D View',
    'location': '',
    'version' : (1,0,1),
    'blender' : (3,0,0),
    'author'  : 'arch4e'
}

classes = [
    MenuShapeKeyMoveBelowSelect,
    SelectDestination,
    SelectShapeKeys,
    ShapeKeyMoveBelowSelect,
    ShapeKeyAlignByPrefix,
    TranscribeShapeKeys,
    # Panel
    TranscribePanel,
    # Property
    TranscribeProps
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.MESH_MT_shape_key_context_menu.append(extended_menu)
    props_register()


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.MESH_MT_shape_key_context_menu.remove(extended_menu)
    props_unregister()


if __name__ == '__main__':
    register()

