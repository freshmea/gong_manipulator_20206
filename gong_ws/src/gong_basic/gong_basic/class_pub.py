import rclpy
from rclpy.node import Node


class M_pub(Node):
    def __init__(self):
        super().__init__("massage_pub")  # 노드 이름
        # timer 등록
        self.create_timer(1, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        self.get_logger().info(f"첫번째 프로그램입니다. {self.count}")
        self.count += 1


def main(args=None):
    rclpy.init(args=args)  # rmw 활성화
    node = M_pub()
    try:
        rclpy.spin(node)  # 블럭 (무한 루프)
    except KeyboardInterrupt:
        node.get_logger().info("키보드 인터럽트")
    finally:
        node.destroy_node()


if __name__ == "__main__":
    main()
