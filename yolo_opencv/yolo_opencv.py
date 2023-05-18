#############################################
# Object detection - YOLO - OpenCV
# Author : Arun Ponnusamy   (July 16, 2018)
# Website : http://www.arunponnusamy.com
############################################


import cv2
import argparse
import numpy as np


def get_output_layers(net):
    layer_names = net.getLayerNames()
    try:
        output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    except:
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    return output_layers


def draw_prediction(
    img, class_id, confidence, x, y, x_plus_w, y_plus_h, COLORS, classes
):
    label = str(classes[class_id])

    color = COLORS[class_id]

    cv2.rectangle(img, (x, y), (x_plus_w, y_plus_h), color, 2)

    cv2.putText(img, label, (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)


def yolo(args):
    if isinstance(args.image, str):
        # assume args.image is file name
        image = cv2.imread(args.image)
    else:
        # assume args.image is numpy.ndarray
        image = args.image

    Width = image.shape[1]
    Height = image.shape[0]

    try:
        scale = args.scale
    except:
        scale = 0.00392

    img_orig = image.copy()

    classes = None

    with open(args.classes, "r") as f:
        classes = [line.strip() for line in f.readlines()]

    COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

    net = cv2.dnn.readNet(args.weights, args.config)

    blob = cv2.dnn.blobFromImage(image, scale, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)

    outs = net.forward(get_output_layers(net))

    class_ids = []
    confidences = []
    boxes = []

    try:
        conf_threshold = args.conf_threshold
    except:
        conf_threshold = 0.5

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > conf_threshold:
                center_x = int(detection[0] * Width)
                center_y = int(detection[1] * Height)
                w = int(detection[2] * Width)
                h = int(detection[3] * Height)
                x = center_x - w / 2
                y = center_y - h / 2
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])

    try:
        nms_threshold = args.nms_threshold
    except:
        nms_threshold = 0.4

    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

    for i in indices:
        try:
            box = boxes[i]
        except:
            i = i[0]
            box = boxes[i]

        x = box[0]
        y = box[1]
        w = box[2]
        h = box[3]
        draw_prediction(
            image,
            class_ids[i],
            confidences[i],
            round(x),
            round(y),
            round(x + w),
            round(y + h),
            COLORS,
            classes,
        )

    try:
        show = args.show
    except:
        show = True

    if show:
        cv2.imshow("object detection", image)
        cv2.waitKey()

        cv2.imwrite("object-detection.jpg", image)
        cv2.destroyAllWindows()

    return img_orig, image, class_ids, boxes, indices, outs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to input image")
    ap.add_argument("-c", "--config", required=True, help="path to yolo config file")
    ap.add_argument(
        "-w", "--weights", required=True, help="path to yolo pre-trained weights"
    )
    ap.add_argument(
        "-cl",
        "--classes",
        required=True,
        help="path to text file containing class names",
    )
    args = ap.parse_args()

    yolo(args)


if __name__ == "__main__":
    main()
