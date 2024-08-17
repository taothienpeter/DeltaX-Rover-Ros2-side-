import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import serial

class Motordriver(Node):
    def __init__(self):
            super().__init__('driver_control')
            self.serial_port = serial.Serial('/dev/ttyUSB0', 115200, timeout=1) 
            self.subscription_ = self.create_subscription(Twist, 'cmd_vel', self.send_serial, 10)
            self.subscription_ 
            #self.publisher_ = self.create_publisher()  
    def send_serial(self, msg):
            self.speed_L = msg.linear.x * 20000 + msg.angular.z * 1000
            self.speed_R = msg.linear.x * 20000 - msg.angular.z * 1000
            self.serial_port.write(f'{float (self.speed_L)}, {float (self.speed_R)}/n'.encode('utf-8').strip())
            self.get_logger().info(f'serial sent: {self.speed_L} , {self.speed_R}')
        

def main(args=None):
    rclpy.init(args=args)
    motor_driver = Motordriver()
    rclpy.spin(motor_driver)
    motor_driver.serial_port.close()
    motor_driver.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
