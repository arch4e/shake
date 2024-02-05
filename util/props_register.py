# -*- coding: utf-8 -*-
import bpy

from ..property.order_management import ShaKe_PG_order_mgmt_prefix
from ..property.create_shape_keys_from_csv import ShaKe_PG_create_shape_keys_from_csv
from ..property.perfect_sync_sk_manager import ShaKe_PG_perfect_sync_sk_list, ShaKe_PG_perfect_sync_sk_manager

properties = {
    bpy.types.Scene: {
        'shake_order_mgmt_active_index': bpy.props.IntProperty(),
        'shake_order_mgmt_prefix_list': bpy.props.CollectionProperty(type=ShaKe_PG_order_mgmt_prefix),
        'shake_create_shape_keys_csv': bpy.props.PointerProperty(type=ShaKe_PG_create_shape_keys_from_csv),
        'shake_perfect_sync_sk_list': bpy.props.CollectionProperty(type=ShaKe_PG_perfect_sync_sk_list),
        'shake_perfect_sync_sk_list_active_index': bpy.props.IntProperty(),
        'shake_perfect_sync_sk_manager': bpy.props.PointerProperty(type=ShaKe_PG_perfect_sync_sk_manager),
    },
}


def register():
    for _type, data in properties.items():
        for attr, prop in data.items():
            if hasattr(_type, attr):
                print(f'WARN: overwrite {_type} {attr}')

            try:
                setattr(_type, attr, prop)
            except Exception as e:
                print(e)


def unregister():
    for _type, data in properties.items():
        for attr in data.keys():
            if hasattr(_type, attr):
                delattr(_type, attr)

