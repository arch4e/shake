import bpy

destination_objects = []
selected_shape_keys = []


class SelectShapeKeys(bpy.types.Operator):
    bl_idname = 'shaku.select_shape_keys'
    bl_label  = 'Select Shape Keys'

    shape_key_name: bpy.props.StringProperty()

    def execute(self, context):
        if self.shape_key_name in selected_shape_keys:
            selected_shape_keys.remove(self.shape_key_name)
        else:
            selected_shape_keys.append(self.shape_key_name)

        return { 'FINISHED' }


class SelectDestination(bpy.types.Operator):
    bl_idname = 'shaku.select_destination_objects'
    bl_label  = 'Select Destination'

    object_name: bpy.props.StringProperty()

    def execute(self, context):
        if self.object_name in destination_objects:
            destination_objects.remove(self.object_name)
        else:
            destination_objects.append(self.object_name)

        return { 'FINISHED' }


class TranscribeShapeKeys(bpy.types.Operator):
    bl_idname = 'shaku.transcribe_shape_keys'
    bl_label  = 'Transcribe Selected Shape Keys to Other Objects'

    def execute(self, context):
        try:
            for object_name in destination_objects:
                _object    = bpy.data.objects[object_name]

                # Create "Base" Shape Key
                if _object.data.shape_keys is None:
                    _object.shape_key_add(name='Basis', from_mix=False)

                # Exclude non-existent shapekeys
                # >>> Switching objects after selecting a shapekey also transfers the shapekey of another object.
                if not context.scene.shaku_transcribe.select_mode_all_sk:
                    existing_shape_keys = bpy.data.objects[
                        context.scene.shaku_transcribe.source
                    ].data.shape_keys.key_blocks.keys()
                    target_shape_keys = list(
                        set(selected_shape_keys) & set(existing_shape_keys)
                    )
                else:
                    target_shape_keys = selected_shape_keys

                # Add Shape Keys
                for shape_key_name in target_shape_keys:
                    if shape_key_name not in _object.data.shape_keys.key_blocks.keys():
                        _object.shape_key_add(name=shape_key_name)

            destination_objects.clear()
            selected_shape_keys.clear()

            return { 'FINISHED' }

        except Exception as e:
            print(e)
            return { 'CANCELLED' }

