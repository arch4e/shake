import bpy

def generate_mesh_prop(self, context):
    items = [(m, m, '') for m in bpy.data.meshes.keys()]
    return items

class TranscribeProps(bpy.types.PropertyGroup):
    source: bpy.props.EnumProperty(
        items = generate_mesh_prop
    )

