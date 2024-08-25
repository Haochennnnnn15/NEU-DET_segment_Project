import os
import json

def convert_json_to_yolo(json_file, img_dir, label_dir):
    # Open and read the JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Extract image information (path, width, height)
    image_path = data['imagePath']
    img_width = data['imageWidth']
    img_height = data['imageHeight']
    
    # Ensure the labels directory exists
    os.makedirs(label_dir, exist_ok=True)
    
    # Generate the corresponding YOLO label file path
    txt_filename = os.path.splitext(image_path)[0] + ".txt"
    txt_filepath = os.path.join(label_dir, txt_filename)
    
    # Open the label file for writing
    with open(txt_filepath, 'w') as txt_file:
        # Iterate over all shapes (segmented regions)
        for shape in data['shapes']:
            # Extract the label name (class)
            label = shape['label']
            if label == "inclusion":
                class_id = 0  # Assume "inclusion" is class 0
                
                # Extract the polygon vertices
                points = shape['points']
                normalized_points = []
                
                # Normalize the vertices to [0, 1] relative to the image dimensions
                for point in points:
                    x = point[0] / img_width
                    y = point[1] / img_height
                    normalized_points.append(f"{x} {y}")
                
                # Write the normalized polygon vertices in YOLO format
                polygon_str = " ".join(normalized_points)
                txt_file.write(f"{class_id} {polygon_str}\n")
    
    # Print confirmation that the file was saved
    print(f"Saved YOLO formatted annotations to: {txt_filepath}")

# Example usage
base_path = r"data path"
sets = ['train', 'validation']

for dataset in sets:
    # Define the directories for annotations, images, and labels
    json_dir = os.path.join(base_path, dataset, 'annotations')
    img_dir = os.path.join(base_path, dataset, 'images', 'inclusion')
    label_dir = os.path.join(base_path, dataset, 'labels', 'inclusion')
    
    # Iterate over all JSON files in the annotations directory
    for json_file in os.listdir(json_dir):
        if json_file.endswith('.json'):
            json_path = os.path.join(json_dir, json_file)
            # Convert JSON annotations to YOLO format
            convert_json_to_yolo(json_path, img_dir, label_dir)
