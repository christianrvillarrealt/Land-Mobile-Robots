#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import cv2

class ImageDisplay(Node):
    def __init__(self):
        super().__init__('image_display')
        self.subscription = self.create_subscription(
            Image,
            'image',
            self.image_callback,
            10
        )
        self.bridge = CvBridge()

    def image_callback(self, msg):
        try:
            # Convert ROS Image message to OpenCV image
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
            cv_image_rotated = cv2.rotate(cv_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
            # Display the image
            cv2.imshow("CoppeliaSim Camera", cv_image_rotated)
            cv2.waitKey(1)

        except Exception as e:
            self.get_logger().error(f"Error processing image: {str(e)}")

def main(args=None):
    rclpy.init(args=args)
    image_display = ImageDisplay()

    try:
        rclpy.spin(image_display)
    except KeyboardInterrupt:
        pass

    image_display.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()