# -*- coding: utf-8 -*-
import bpy

from .operator.context_menu_extention import ShaKe_OT_align_by_prefix, ShaKe_OT_move_shape_key_below_selected
from .operator.create_shape_keys_from_csv import ShaKe_OT_create_shape_keys_from_csv
from .operator.order_management import (
    ShaKe_OT_add_prefix,
    ShaKe_OT_move_prefix_down,
    ShaKe_OT_move_prefix_up,
    ShaKe_OT_rearrange_by_prefix_list,
    ShaKe_OT_remove_prefix,
    ShaKe_OT_sync_selected_obj_prefix_list
)
from .operator.selector import ShaKe_OT_select_shape_key
from .operator.transcribe import ShaKe_OT_select_destination, ShaKe_OT_select_shape_keys, ShaKe_OT_transcribe_shape_keys
from .property.create_shape_keys_from_csv import ShaKe_PG_create_shape_keys_from_csv
from .property.order_management import ShaKe_PG_order_mgmt_prefix
from .property.transcribe import ShaKe_PG_transcribe
from .ui.context_menu_extention import ShaKe_MT_move_shape_key_below_selected, ShaKe_MT_shape_keys_extended_menu
from .ui.create_shape_keys_from_csv import ShaKe_PT_create_shape_keys_from_csv
from .ui.order_management import ShaKe_PT_order_management, UI_UL_ShaKe_order_management
from .ui.selector import ShaKe_PT_shape_keys_selector
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


# Menus and Panels are displayed in the order of registration,
# so they are not arranged alphabetically.
classes = [
    ShaKe_MT_move_shape_key_below_selected,
    ShaKe_OT_add_prefix,
    ShaKe_OT_align_by_prefix,
    ShaKe_OT_create_shape_keys_from_csv,
    ShaKe_OT_move_prefix_down,
    ShaKe_OT_move_prefix_up,
    ShaKe_OT_move_shape_key_below_selected,
    ShaKe_OT_rearrange_by_prefix_list,
    ShaKe_OT_remove_prefix,
    ShaKe_OT_select_destination,
    ShaKe_OT_select_shape_key,
    ShaKe_OT_select_shape_keys,
    ShaKe_OT_sync_selected_obj_prefix_list,
    ShaKe_OT_transcribe_shape_keys,
    ShaKe_PG_create_shape_keys_from_csv,
    ShaKe_PG_order_mgmt_prefix,
    ShaKe_PG_transcribe,
    ShaKe_PT_create_shape_keys_from_csv,
    ShaKe_PT_order_management,
    ShaKe_PT_shape_keys_selector,
    ShaKe_PT_transcribe,
    UI_UL_ShaKe_order_management,
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

