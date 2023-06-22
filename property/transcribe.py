# -*- coding: utf-8 -*-
import bpy


def generate_object_prop(self, context):
    try:
        items = [(n, n, '') for (n, d) in bpy.data.objects.items() if d.type == 'MESH']
        return items
    except Exception as e:
        print(e)
        return []


class TranscribeProps(bpy.types.PropertyGroup):
    select_mode_all_sk: bpy.props.BoolProperty(default=False)

    source: bpy.props.EnumProperty(
        items=generate_object_prop
    )

