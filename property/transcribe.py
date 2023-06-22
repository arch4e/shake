import bpy


def generate_mesh_prop(self, context):
    items = [(m, m, '') for m in bpy.data.meshes.keys()]
    return items


class TranscribeProps(bpy.types.PropertyGroup):
    select_mode_all_sk: bpy.props.BoolProperty(default=False)

    source: bpy.props.EnumProperty(
        items=generate_mesh_prop
    )

