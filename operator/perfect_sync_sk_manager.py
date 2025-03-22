# -*- coding: utf-8 -*-
import bpy

from ..util.perfect_sync_definition import PERFECT_SYNC_SHAPE_KEYS


class ShaKe_OT_init_perfect_sync(bpy.types.Operator):
    bl_idname = 'shake.init_perfect_sync'
    bl_label  = ''

    def execute(self, context):
        context.scene.shake_perfect_sync_sk_list.clear()

        for i in range(len(PERFECT_SYNC_SHAPE_KEYS)):
            _item = context.scene.shake_perfect_sync_sk_list.add()
            _item.name = PERFECT_SYNC_SHAPE_KEYS[i]

        return {'FINISHED'}


class ShaKe_OT_add_perfect_sync_shape_key(bpy.types.Operator):
    bl_idname = 'shake.add_perfect_sync_shape_key'
    bl_label  = ''

    shape_key_name: bpy.props.StringProperty()

    def execute(self, context):
        context.active_object.shape_key_add(name=self.shape_key_name, from_mix=False)
        return {'FINISHED'}


