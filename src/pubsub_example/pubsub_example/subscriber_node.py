import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node')

        self.create_subscription(
            String, '/example_topic', self.subscriber_callback, 10)

        self.get_logger().info("Subscriber node has been started.")

    def subscriber_callback(self, ros_msg):
        self.get_logger().info(ros_msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
