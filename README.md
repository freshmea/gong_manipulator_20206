# gong_manipulator_20206
- 로보티즈의 매니퓰레이터를 실습하는 수업
- [교육생공유슬라이드](https://docs.google.com/presentation/d/1u1cTo7-lzOgn1OTffYmj8k5heEegl7OFczK4jscYZt8/edit?usp=sharing)

---

# 2026-07-20

---

- wsl 을 설치 (Ubuntu 24.04)
- github 아이디를 만들고 repository를 생성
- git clone 을 해서 wsl 에 복사
- Vscode 설치 해서 remote wsl 로 접속
- github 계정 연동
- ros2 설치 - jazzy
- turtlesim 실습
- ros2 cli 실습
  - node: list, info
  - topic: list, info ,echo, pub, sub, bw, hz
  - service: list, info, call
  - interface: proto
- rqt 실습: rqt_graph, topic monitor,

```shell
ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"

```