# -*- coding: utf-8 -*-
import bpy
import re

from .common import BasePanel
from ..util.perfect_sync_definition import PERFECT_SYNC_SHAPE_KEYS


class ShaKe_PT_perfect_sync_sk_manager(BasePanel, bpy.types.Panel):
    bl_idname = 'VIEW3D_PT_ShaKe_perfect_sync_sk_manager'
    bl_label  = 'Perfect Sync'

    @classmethod
    def poll(cls, context):
        return context.object and context.object.data.shape_keys is not None

    def draw(self, context):
        col = self.layout.column()
        col.enabled = context.object.mode != 'EDIT' and context.object.data.shape_keys is not None

        _total_shape_key_count = len(context.active_object.data.shape_keys.key_blocks.keys())
        _perfect_sync_sk_count, _custom_sk_count = count_exist_shape_keys(context)
        col.label(text='Statistics', icon='TRIA_DOWN')
        box = col.box()
        box.label(text=f'Total Shape Keys: {_total_shape_key_count}')
        box.label(text=f'P-Sync Shape Keys: {_perfect_sync_sk_count}')
        box.label(text=f'Custom Shape Keys: {_custom_sk_count}')

        col.separator()

        col.label(text='Shape Keys for Active Objects', icon='TRIA_DOWN')
        col.prop(
            context.scene.shake_perfect_sync_sk_manager,
            'checker_enabled',
            text='Enable/Disable (heavy)',
            icon='CHECKBOX_HLT' if context.scene.shake_perfect_sync_sk_manager.checker_enabled else 'CHECKBOX_DEHLT',
        )
        if context.scene.shake_perfect_sync_sk_manager.checker_enabled:
            if len(context.scene.shake_perfect_sync_sk_list) != len(PERFECT_SYNC_SHAPE_KEYS):
                col.operator('shake.init_perfect_sync_init', text='init')

            col.template_list(
                'UI_UL_ShaKe_perfect_sync_sk_management',
                '',
                context.scene,
                'shake_perfect_sync_sk_list',
                context.scene,
                'shake_perfect_sync_sk_list_active_index',
                rows=5
            )


class UI_UL_ShaKe_perfect_sync_sk_management(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        # check the shape key exists
        # note: property updates cannot be done from 'context',
        #       this code sequentially evaluations rather than pre-evaluations
        key_blocks = context.active_object.data.shape_keys.key_blocks.keys()
        match_count = len(list(filter(lambda x: re.fullmatch(rf'{item.name}', x, re.IGNORECASE) is not None, key_blocks)))

        # draw
        row = layout.row()
        row.label(text=f'{item.name}', icon='CHECKMARK' if match_count > 0 else 'NONE')


def count_exist_shape_keys(context):
    pssk_count = 0
    cssk_count = 0
    key_blocks = context.active_object.data.shape_keys.key_blocks.keys()
    for key_name in key_blocks:
        match_count = len(list(filter(lambda x: re.fullmatch(rf'{key_name}', x, re.IGNORECASE) is not None, PERFECT_SYNC_SHAPE_KEYS)))
        if match_count != 1:
            print(match_count)
        if match_count > 0:
            pssk_count += 1
        else:
            cssk_count += 1

    return pssk_count, cssk_count

