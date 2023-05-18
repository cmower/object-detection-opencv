from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="yolo_opencv",
    description="YOLO Object detection with OpenCV and Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="1.0.0",
    author="Arun Ponnusamy, Christopher E. Mower",
    author_email="christopher.mower@kcl.ac.uk",
    url="https://github.com/cmower/object-detection-opencv",
    packages=["yolo_opencv"],
    license="MIT License",
    entry_points={
        "console_scripts": [
            "yolo_opencv = yolo_opencv.yolo_opencv:main",
        ],
    },
    install_requires=[
        "opencv-contrib-python",
        "numpy",
    ],
)
