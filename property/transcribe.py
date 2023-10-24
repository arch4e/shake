# -*- coding: utf-8 -*-
import bpy


def generate_collection_prop(self, context):
    try:
        items = [(c, c, '') for c in bpy.data.collections.keys()]
        items.insert(0, ('ALL', 'ALL', ''))
        return items
    except Exception as e:
        print(e)
        return []


def generate_object_prop(self, context):
    try:
        items = [(n, n, '') for (n, d) in bpy.data.objects.items() if d.type == 'MESH']
        return items
    except Exception as e:
        print(e)
        return []


class TranscribeProps(bpy.types.PropertyGroup):
    source_mode_single_object: bpy.props.BoolProperty(default=False)

    source: bpy.props.EnumProperty(
        items=generate_object_prop
    )

    filter_collection: bpy.props.EnumProperty(
        items=generate_collection_prop
    )

