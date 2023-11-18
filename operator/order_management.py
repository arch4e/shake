# -*- coding: utf-8 -*-
import bpy
import re


class ShaKe_OT_add_prefix(bpy.types.Operator):
    bl_idname = 'shake.add_prefix'
    bl_label  = ''

    def execute(self, context):
        context.scene.shake_order_mgmt_prefix_list.add()
        return { 'FINISHED' }


class ShaKe_OT_move_prefix_down(bpy.types.Operator):
    bl_idname = 'shake.move_prefix_down'
    bl_label  = ''

    def execute(self, context):
        index = context.scene.shake_order_mgmt_active_index
        data  = context.scene.shake_order_mgmt_prefix_list

        if index < len(data) - 1:
            data.move(index, index + 1)
            context.scene.shake_order_mgmt_active_index += 1

        return { 'FINISHED' }


class ShaKe_OT_move_prefix_up(bpy.types.Operator):
    bl_idname = 'shake.move_prefix_up'
    bl_label  = ''

    def execute(self, context):
        index = context.scene.shake_order_mgmt_active_index
        data  = context.scene.shake_order_mgmt_prefix_list

        if index > 0:
            data.move(index, index - 1)
            context.scene.shake_order_mgmt_active_index -= 1

        return { 'FINISHED' }


class ShaKe_OT_rearrange_by_prefix_list(bpy.types.Operator):
    bl_idname = 'shake.rearrange_by_prefix_list'
    bl_label  = ''

    def execute(self, context):
        shape_keys = context.active_object.data.shape_keys.key_blocks.keys()
        backup_active_shape_key_name = shape_keys[
            bpy.context.object.active_shape_key_index
        ]
        user_defined_prefix_list = context.scene.shake_order_mgmt_prefix_list.keys()
        sorted_tail_index = 0

        for prefix in user_defined_prefix_list:
            prefix_included_shape_key_index = [index for index, name in enumerate(shape_keys) if re.match(rf'^{prefix}', name)]
            for current_index in prefix_included_shape_key_index:
                move_steps = current_index - sorted_tail_index
                if move_steps >= 0:
                    bpy.context.object.active_shape_key_index = current_index
                    for _ in range(move_steps):
                        bpy.ops.object.shape_key_move(type='UP')
                    # update tail index
                    # move_steps = 0 is in the correct position and does not need to be moved
                    sorted_tail_index += 1
                shape_keys = context.active_object.data.shape_keys.key_blocks.keys()


        bpy.context.object.active_shape_key_index = shape_keys.index(backup_active_shape_key_name)

        return { 'FINISHED' }


class ShaKe_OT_remove_prefix(bpy.types.Operator):
    bl_idname = 'shake.remove_prefix'
    bl_label  = ''

    def execute(self, context):
        context.scene.shake_order_mgmt_prefix_list.remove(
            context.scene.shake_order_mgmt_active_index
        )

        return { 'FINISHED' }


class ShaKe_OT_sync_selected_obj_prefix_list(bpy.types.Operator):
    bl_idname = 'shake.sync_selected_obj_prefix'
    bl_label  = 'Sync Shape Key Prefix'

    def execute(self, context):
        obj_prefix_list = dict.fromkeys(map(lambda x: re.split('\_|\.', x)[0], context.active_object.data.shape_keys.key_blocks.keys()))

        context.scene.shake_order_mgmt_prefix_list.clear()
        for prefix in obj_prefix_list:
            context.scene.shake_order_mgmt_prefix_list.add().name = prefix

        return { 'FINISHED' }

