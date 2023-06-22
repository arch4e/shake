# -*- coding: utf-8 -*-
class BasePanel(object):
    bl_space_type  = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category    = 'ShaKU'

    @classmethod
    def poll(cls, context):
        return True

