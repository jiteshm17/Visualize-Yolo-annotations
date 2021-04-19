# Visualize-Yolo-annotations
A simple tool that will help visualize bounding boxes in darknet/yolo format. The only package needed for this is work is OpenCV


# Usage

`python vis_bbox.py --folder_path path/to/folder --classes path/to/classes.names --save_path folder_to_save/`

`--folder_path` is the path to the folder containing the images and the labels  
`--classes` is the path to the `classes.names` file  
`--save_path` is the path where the saved images will be stored (will be created automatically if folder does not exist)
