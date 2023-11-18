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
        active_object_shape_keys = context.active_object.data.shape_keys.key_blocks.keys()
        backup_active_shape_key_name = active_object_shape_keys[
            bpy.context.object.active_shape_key_index
        ]
        user_defined_prefix_list = context.scene.shake_order_mgmt_prefix_list.keys()
        sorted_tail_index = 0

        shape_keys_dict = generate_shape_keys_dict_with_longest_match()

        for _prefix in user_defined_prefix_list:
            prefix_included_shape_key_index = [active_object_shape_keys.index(x) for x in shape_keys_dict[_prefix]]
            for current_index in prefix_included_shape_key_index:
                move_steps = current_index - sorted_tail_index
                if move_steps >= 0:
                    bpy.context.object.active_shape_key_index = current_index
                    for _ in range(move_steps):
                        bpy.ops.object.shape_key_move(type='UP')
                    # update tail index
                    # move_steps = 0 is in the correct position and does not need to be moved
                    sorted_tail_index += 1
                active_object_shape_keys = context.active_object.data.shape_keys.key_blocks.keys()

        bpy.context.object.active_shape_key_index = active_object_shape_keys.index(backup_active_shape_key_name)

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
        obj_prefix_list = dict.fromkeys(map(lambda x: re.split('\_|\.', x)[0], context.active_object.data.shape_keys.key_blocks.keys())) # noqa: W605

        context.scene.shake_order_mgmt_prefix_list.clear()
        for prefix in obj_prefix_list:
            context.scene.shake_order_mgmt_prefix_list.add().name = prefix

        return { 'FINISHED' }


def generate_shape_keys_dict_with_longest_match():
    active_object_shape_keys_list = bpy.context.active_object.data.shape_keys.key_blocks.keys()
    user_defined_prefix_list      = bpy.context.scene.shake_order_mgmt_prefix_list.keys()

    shape_keys_dict = {}
    for _prefix in sorted(user_defined_prefix_list, key=len, reverse=True):
        shape_keys_dict[_prefix] = []
        for _shape_key in [x for x in active_object_shape_keys_list if re.match(rf'^{_prefix}', x)]:
            shape_keys_dict[_prefix].append(_shape_key)
            active_object_shape_keys_list.remove(_shape_key)

    return shape_keys_dict
