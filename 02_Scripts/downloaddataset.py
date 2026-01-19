from roboflow import Roboflow
import torch
print(f"Is cuda available for training?: {torch.cuda.is_available()}")

rf = Roboflow(api_key="mTwL8ga72R2LP9j2TkRt")
project = rf.workspace("pmec").project("rooftop-segmentation-nbosn")
version = project.version(8)
dataset = version.download("yolov8-obb")       

import yaml

with open(f'{dataset.location}/data.yaml', 'r') as file:
    data = yaml.safe_load(file)

data['path'] = dataset.location

with open(f'{dataset.location}/data.yaml', 'w') as file:
    yaml.dump(data, file, sort_keys=False)