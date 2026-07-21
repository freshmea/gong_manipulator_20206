from setuptools import find_packages, setup

package_name = "gong_basic"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="choi su gil",
    maintainer_email="freshmea@naver.com",
    description="gongju university ROS2 basic library",
    license="Apache 2.0",
    extras_require={
        "test": [
            "pytest",
        ],
    },
    entry_points={
        "console_scripts": [
            "simple_pub = gong_basic.simple_pub:main",
            "class_pub = gong_basic.class_pub:main",
        ],
    },
)
