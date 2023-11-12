# -*- coding: utf-8 -*-
import bpy

from .operator.context_menu_extention import ShaKe_OT_align_by_prefix, ShaKe_OT_move_shape_key_below_selected
from .operator.transcribe import ShaKe_OT_select_destination, ShaKe_OT_select_shape_keys, ShaKe_OT_transcribe_shape_keys
from .property.transcribe import ShaKe_PG_transcribe
from .ui.context_menu_extention import ShaKe_MT_move_shape_key_below_selected, ShaKe_MT_shape_keys_extended_menu
from .ui.transcribe import ShaKe_PT_transcribe
from .util.props_register import register as props_register, unregister as props_unregister


bl_info = {
    'name'    : 'ShaKe',
    'category': '3D View',
    'location': '',
    'version' : (1,0,0),
    'blender' : (3,0,0),
    'author'  : 'arch4e'
}


classes = [
    ShaKe_MT_move_shape_key_below_selected,
    ShaKe_OT_align_by_prefix,
    ShaKe_OT_move_shape_key_below_selected,
    ShaKe_OT_select_destination,
    ShaKe_OT_select_shape_keys,
    ShaKe_OT_transcribe_shape_keys,
    ShaKe_PG_transcribe,
    ShaKe_PT_transcribe,
]


def register():
    # Operator
    for cls in classes:
        bpy.utils.register_class(cls)

    # Menu
    bpy.types.MESH_MT_shape_key_context_menu.append(ShaKe_MT_shape_keys_extended_menu)

    # Property
    props_register()


def unregister():
    # Operator
    for cls in classes:
        bpy.utils.unregister_class(cls)

    # Menu
    bpy.types.MESH_MT_shape_key_context_menu.remove(ShaKe_MT_shape_keys_extended_menu)

    # Property
    props_unregister()


if __name__ == '__main__':
    register()

