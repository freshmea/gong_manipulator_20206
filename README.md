# gong_manipulator_20206
- 로보티즈의 매니퓰레이터를 실습하는 수업
- [교육생공유슬라이드](https://docs.google.com/presentation/d/1u1cTo7-lzOgn1OTffYmj8k5heEegl7OFczK4jscYZt8/edit?usp=sharing)
- [사전사후평가](https://forms.gle/8AmhKaho7VugqqrDA)

---

## 2026-07-20

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

```bash
ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"

```

---

## 2026-07-21

---

- 1교시: 복습, ros2 common package
- 2교시: 중요 컨셉(DDS, node spin, state)
- 3교시: RMW architecture
- 4교시: Node, Topic, Service, Action 개념
- 5교시: 패키지 작성 ( ros2 pkg create)
- 6교시: simple node 작성(publisher, subscriber)
- 7교시: Header class time pub 작성, 5개 노드 실습
- 8교시: 터틀심 움직이기

---

## 2026-07-22

---

- 1교시: 복습
- 2교시: DDS wsl 에서 설정해야 할 내용 설명
- 3교시: interface 정의, msg, srv 작성
- 4교시: service thread server 작성
- 5교시: service client 작성()
- 6교시:
- 7교시:
- 8교시:

## 추가 해야 할 작업
- service 교안 부재
- action 교안 부재
- launch 교안 부재