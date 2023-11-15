# -*- coding: utf-8 -*-
import bpy


from .common import BasePanel


class ShaKe_PT_order_management(BasePanel, bpy.types.Panel):
    bl_idname = 'VIEW3D_PT_ShaKe_order_management'
    bl_label  = 'Order Management'

    @classmethod
    def poll(cls, context):
        return context.object

    def draw(self, context):
        col = self.layout.column()
        col.enabled = context.object.mode != 'EDIT'
        row = col.row()

        row.template_list('UI_UL_ShaKe_order_management', '', context.scene, 'shake_order_mgmt_prefix_list', context.scene, 'shake_order_mgmt_active_index', rows=5)

        _col = row.column()
        _col.operator('shake.sync_selected_obj_prefix', icon='FILE_REFRESH', text='')
        _col.operator('shake.add_prefix', icon='ADD', text='')
        _col.operator('shake.remove_prefix', icon='REMOVE', text='')
        if len(context.scene.shake_order_mgmt_prefix_list) > 0:
            _col.separator()
            _col.operator('shake.move_prefix_up', icon='TRIA_UP', text='')
            _col.operator('shake.move_prefix_down', icon='TRIA_DOWN', text='')

        _col = col.column()
        _col.separator()
        _col.operator('shake.rearrange_by_prefix_list', text='Rearrange')


class UI_UL_ShaKe_order_management(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        _text = ''
        if item.name == '':
            _text = 'Input Prefix'
        layout.prop(item, 'name', text=_text, emboss=False)
