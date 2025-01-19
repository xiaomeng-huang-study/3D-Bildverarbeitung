import open3d as o3d
import numpy as np

def save_view(vis):
    """Callback function to save the current view."""
    ctr = vis.get_view_control()
    param = ctr.convert_to_pinhole_camera_parameters()
    o3d.io.write_pinhole_camera_parameters("saved_view.json", param)
    print("View saved as 'saved_view.json'")
    return False

def main():
    # Load a sample point cloud
    # pcd = o3d.io.read_point_cloud(o3d.data.PCDPointCloud().path)
    pcd = o3d.io.read_point_cloud("pcds_processed/point_cloud_030.pcd")

    # Create a Visualizer with key callback
    visualizer = o3d.visualization.VisualizerWithKeyCallback()
    visualizer.create_window(width=1440, height=900)
    visualizer.set_full_screen(fullscreen = False)
    visualizer.add_geometry(pcd)

    # Add key callback for saving view with 's'
    visualizer.register_key_callback(ord("S"), save_view)

    print("Adjust the view with the mouse and press 's' to save the current view.")

    # Run the visualizer
    visualizer.run()
    visualizer.destroy_window()

if __name__ == "__main__":
    main()
