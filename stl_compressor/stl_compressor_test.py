import os
import open3d as o3d

target_number_of_triangles = 1000

current_directory = os.getcwd()

input_directory = os.path.join(current_directory, 'test/input')
output_directory = os.path.join(current_directory, 'test/output')

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for stl_file in os.listdir(input_directory):
    if stl_file.lower().endswith(".stl"):
        mesh = o3d.io.read_triangle_mesh(os.path.join(input_directory, stl_file))
        simplified_mesh = mesh.simplify_quadric_decimation(target_number_of_triangles)
        simplified_mesh.compute_triangle_normals()
        simplified_mesh.compute_vertex_normals()
        output_file_path = os.path.join(output_directory, stl_file)
        o3d.io.write_triangle_mesh(output_file_path, simplified_mesh)
