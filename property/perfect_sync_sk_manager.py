# -*- coding: utf-8 -*-
import bpy


class ShaKe_PG_perfect_sync_sk_list(bpy.types.PropertyGroup):
    # name: bpy.props.StringProperty(default='')
    # >>> "name" is pre-defined attributes
    exists: bpy.props.BoolProperty(default=False)


class ShaKe_PG_perfect_sync_sk_manager(bpy.types.PropertyGroup):
    checker_enabled: bpy.props.BoolProperty(default=True)

