# -*- coding: utf-8 -*-
import bpy
import random


def generate_shape_keys(num):
    prefix_list = ['', 'A_', 'B_', 'C_', 'D_']
    bpy.context.active_object.shape_key_add(name='Basis', from_mix=False)
    for i in range(num):
        bpy.context.active_object.shape_key_add(name=f'{random.choice(prefix_list)}KEY', from_mix=False)
