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
from .operator.perfect_sync_sk_manager import ShaKe_OT_init_perfect_sync_init
from .property.create_shape_keys_from_csv import ShaKe_PG_create_shape_keys_from_csv
from .property.order_management import ShaKe_PG_order_mgmt_prefix
from .property.perfect_sync_sk_manager import ShaKe_PG_perfect_sync_sk_list, ShaKe_PG_perfect_sync_sk_manager
from .ui.context_menu_extention import ShaKe_MT_move_shape_key_below_selected, ShaKe_MT_shape_keys_extended_menu
from .ui.create_shape_keys_from_csv import ShaKe_PT_create_shape_keys_from_csv
from .ui.order_management import ShaKe_PT_order_management, UI_UL_ShaKe_order_management
from .ui.perfect_sync_sk_manager import ShaKe_PT_perfect_sync_sk_manager, UI_UL_ShaKe_perfect_sync_sk_management
from .util.props_register import register as props_register, unregister as props_unregister


bl_info = {
    'name'    : 'ShaKe',
    'category': '3D View',
    'location': '',
    'version' : (2,1,0),
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
    ShaKe_OT_init_perfect_sync_init,
    ShaKe_OT_move_prefix_down,
    ShaKe_OT_move_prefix_up,
    ShaKe_OT_move_shape_key_below_selected,
    ShaKe_OT_rearrange_by_prefix_list,
    ShaKe_OT_remove_prefix,
    ShaKe_OT_sync_selected_obj_prefix_list,
    ShaKe_PG_create_shape_keys_from_csv,
    ShaKe_PG_order_mgmt_prefix,
    ShaKe_PG_perfect_sync_sk_list,
    ShaKe_PG_perfect_sync_sk_manager,
    ShaKe_PT_create_shape_keys_from_csv,
    ShaKe_PT_order_management,
    ShaKe_PT_perfect_sync_sk_manager,
    UI_UL_ShaKe_order_management,
    UI_UL_ShaKe_perfect_sync_sk_management,
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

