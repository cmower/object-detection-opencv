# Object detection using deep learning with OpenCV and Python 

OpenCV `dnn` module supports running inference on pre-trained deep learning models from popular frameworks like Caffe, Torch and TensorFlow. 

When it comes to object detection, popular detection frameworks are
 * YOLO
 * SSD
 * Faster R-CNN
 
 Support for running YOLO/DarkNet has been added to OpenCV dnn module recently. 
 
## Install

1. Clone repository: `$ git@github.com:cmower/object-detection-opencv.git`
2. Change directory: `$ cd object-detection-opencv`
3. Install: `$ pip install .`

## Usage

Either you can use the command line interface `yolo_opencv` (see examples below) or import the package using

```python
import yolo_opencv
```

## YOLO (You Only Look Once)
 
 Download the pre-trained YOLO v3 weights file from this [link](https://pjreddie.com/media/files/yolov3.weights) and place it in the current directory or you can directly download to the current directory in terminal using
 
 `$ wget https://pjreddie.com/media/files/yolov3.weights`
 
 Provided all the files are in the current directory, below command will apply object detection on the input image `dog.jpg`.
 
```
$ yolo_opencv --image dog.jpg --config yolov3.cfg --weights yolov3.weights --classes yolov3.txt
```
 
 
 **Command format** 

```
$ yolo_opencv --image /path/to/input/image --config /path/to/config/file --weights /path/to/weights/file --classes /path/to/classes/file_
```
 
 Checkout the [blog post](https://towardsdatascience.com/yolo-object-detection-with-opencv-and-python-21e50ac599e9) to learn more.
 
### sample output :
 ![](object-detection.jpg)
 
Checkout the object detection implementation available in [cvlib](http:cvlib.net) which enables detecting common objects in the context through a single function call `detect_common_objects()`.
 
 
 (_SSD and Faster R-CNN examples will be added soon_)
