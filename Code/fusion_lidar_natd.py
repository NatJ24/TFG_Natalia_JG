import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2, PointField
from carla_ros_bridge.sensor import create_cloud 
from rosgraph_msgs.msg import Clock

import ros2_numpy as rnp
import carla
import numpy as np
import time


class LidarFusionAlberto(Node):

    def __init__(self):
        super().__init__('lidar_fusion_alberto')
        self.time_step_carla = 0.05
        self.first = True

        # Variables para almacenar arrays de LIDAR
        self.lidar_arrays = [None] * 8

        # Conexión a CARLA
        client = carla.Client('localhost', 2000)
        client.set_timeout(10.0)
        self.world = client.get_world()

        # Modo síncrono
        settings = self.world.get_settings()
        settings.synchronous_mode = True
        settings.fixed_delta_seconds = self.time_step_carla
        self.world.apply_settings(settings)

        # Publisher
        self.publisher = self.create_publisher(PointCloud2, '/carla/ego_vehicle/LIDAR', 10)

        # Subscriptores para los 8 LIDARs
        for i in range(8):
            topic = f'/carla/ego_vehicle/LIDAR_{i}'
            self.create_subscription(PointCloud2, topic, lambda msg, i=i: self.lidar_callback(msg, i), 10)

        # Subscripción al reloj
        self.create_subscription(Clock, '/clock', self.publish_fusion_lidar, 10)

    def lidar_callback(self, msg, idx):
        data = rnp.numpify(msg)
        try:
            # Extrae campos: x, y, z, intensity (convirtiendo a array plano)
            points = np.zeros((data.shape[0], 4), dtype=np.float32)
            points[:, 0] = data['x']
            points[:, 1] = data['y']
            points[:, 2] = data['z']
            points[:, 3] = data['intensity']
            self.lidar_arrays[idx] = points
            self.get_logger().info(f"LIDAR_{idx} received. Shape: {points.shape}")
        except Exception as e:
            self.get_logger().error(f"Error processing LIDAR_{idx}: {e}")

    def publish_fusion_lidar(self, clock_msg):
        if any(arr is None for arr in self.lidar_arrays):
            self.get_logger().warn("Not all LIDAR data is available yet.")
            return

        try:
            all_lidar_data = np.concatenate(self.lidar_arrays, axis=0)
        except ValueError as e:
            self.get_logger().error(f"Error concatenating arrays: {e}")
            return

        self.get_logger().info(f"Publishing Fusion LiDAR with shape: {all_lidar_data.shape}")

        # Crear el mensaje PointCloud2
        header = rclpy.time.Time(clock_msg.clock).to_msg()
        fields = [
            PointField(name='x', offset=0, datatype=PointField.FLOAT32, count=1),
            PointField(name='y', offset=4, datatype=PointField.FLOAT32, count=1),
            PointField(name='z', offset=8, datatype=PointField.FLOAT32, count=1),
            PointField(name='intensity', offset=12, datatype=PointField.FLOAT32, count=1),
        ]
        cloud_msg = create_cloud(header=clock_msg.header, fields=fields, points=all_lidar_data)
        cloud_msg.header.frame_id = 'ego_vehicle'
        self.publisher.publish(cloud_msg)

        if self.first:
            self.get_logger().info(f"First publish width: {cloud_msg.width}")
            self.first = False


def main(args=None):
    rclpy.init(args=args)
    lidar_fusion = LidarFusionAlberto()
    rclpy.spin(lidar_fusion)
    lidar_fusion.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
