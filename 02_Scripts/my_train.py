
# Imports

from ultralytics import YOLO
from roboflow import Roboflow
import torch

#Training


def main():
    #Check for GPU
    print(f"Is cuda available for training?: {torch.cuda.is_available()}")
    
    
    # Load the model
    model = YOLO("yolov8n-obb.pt")

    results = model.train(
    data="Master_Rooftop_Dataset/data.yaml",
    epochs=300,
    imgsz=640,
    patience=50,    # If no improvement in 50 epochs, stop early
    save_period=10, # Save a checkpoint every 10 epochs
    overlap_mask=True, # Helpful for OBB if roofs are close together
    project="rooftop_project", # Names your output folder
    name="bootstrap_v1"
)

if __name__ == '__main__':
    main()