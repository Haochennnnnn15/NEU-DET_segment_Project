import os
import shutil

# Define the folder paths
train_images_path = r"data path"
validation_images_path = r"data path"
train_annotations_path = r"data path"
validation_annotations_path = r"data path"

# Create target folders if they don't already exist
os.makedirs(train_annotations_path, exist_ok=True)
os.makedirs(validation_annotations_path, exist_ok=True)

# Move JSON files from the train folder to the annotations folder
for file_name in os.listdir(train_images_path):
    if file_name.endswith('.json'):
        source_file = os.path.join(train_images_path, file_name)
        destination_file = os.path.join(train_annotations_path, file_name)
        shutil.move(source_file, destination_file)

# Move JSON files from the validation folder to the annotations folder
for file_name in os.listdir(validation_images_path):
    if file_name.endswith('.json'):
        source_file = os.path.join(validation_images_path, file_name)
        destination_file = os.path.join(validation_annotations_path, file_name)
        shutil.move(source_file, destination_file)

print("All JSON files have been successfully moved.")
