import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')

        self.publisher_ = self.create_publisher(String, "/example_topic", 10)
        self.create_timer(0.01, self.timer_callback)

        self.get_logger().info("Publisher node has been started.")

    def timer_callback(self):
        input_text = input()

        ros_msg = String()
        ros_msg.data = input_text

        self.publisher_.publish(ros_msg)


def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
