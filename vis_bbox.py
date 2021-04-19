import os
import cv2
import argparse
import json


def main():

    parser = argparse.ArgumentParser(description='Verify Yolo Annotations')
    parser.add_argument('--folder_path', type=str, help='Path to folder containing images and the corresponding labels')
    parser.add_argument('--classes', type=str, help='Path to classes.names file')
    parser.add_argument('--save_path', type=str, help='Path to save annotated images')
    args = parser.parse_args()

    with open(args.classes) as class_names:
        classes = class_names.readlines()
    
    classes = [x.strip() for x in classes]
    
    class_names = {}
    for idx,name in enumerate(classes):
        class_names[name] = idx
    
    class_names = {v: k for k, v in class_names.items()}
    
    print(class_names)

    args = parser.parse_args()

    os.makedirs(args.save_path,exist_ok=True)

    all_files = os.listdir(args.folder_path)
    annotations, images = [], []

    for file in all_files:
        if '.txt' in file:
            annotations.append(file)
        elif '.jpg' or '.jpeg' or '.png' in file:
            images.append(file)

    if len(images) > len(annotations):
        print("Some images dont have annotations")
        return

    elif len(images) < len(annotations):
        print("There are more annotations than images")
        return

    images.sort()
    annotations.sort()

    color = (255,0,0)
    for (image, annotation) in zip(images, annotations):
        img = cv2.imread(os.path.join(args.folder_path,image))
        height, width, _ = img.shape
        with open(os.path.join(args.folder_path,annotation)) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        for annot in content:
            annot = annot.split()
            class_idx = int(annot[0])
            x,y,w,h = float(annot[1]),float(annot[2]),float(annot[3]),float(annot[4])
            xmin = int((x*width) - (w * width)/2.0)
            ymin = int((y*height) - (h * height)/2.0)
            xmax = int((x*width) + (w * width)/2.0)
            ymax = int((y*height) + (h * height)/2.0)
            cv2.rectangle(img, (xmin, ymin), (xmax, ymax), color, 2)
            cv2.putText(img, class_names[int(class_idx)], (xmin, ymin - 5), cv2.FONT_HERSHEY_SIMPLEX,0.5, color, 2)

        # cv2.imshow(image, img)
        # cv2.waitKey(0)

        cv2.imwrite(os.path.join(args.save_path,image), img)
        print("saving image",image)
    
    print("Done")


if __name__ == '__main__':
	main()
			
