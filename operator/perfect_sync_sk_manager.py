# -*- coding: utf-8 -*-
import bpy

from ..util.perfect_sync_definition import PERFECT_SYNC_SHAPE_KEYS


class ShaKe_OT_init_perfect_sync_init(bpy.types.Operator):
    bl_idname = 'shake.init_perfect_sync_init'
    bl_label  = ''

    def execute(self, context):
        for _ in context.scene.shake_perfect_sync_sk_list.items():
            context.scene.shake_perfect_sync_sk_list.remove(0)

        for i in range(len(PERFECT_SYNC_SHAPE_KEYS)):
            _item = context.scene.shake_perfect_sync_sk_list.add()
            _item.name = PERFECT_SYNC_SHAPE_KEYS[i]

        return {'FINISHED'}

