from ultralytics import YOLO

def run_inference():
   
    model = YOLO("rooftop_project/bootstrap_v1/weights/best.pt")

    # 2. Run prediction on your folder of 100 images
    results = model.predict(
        source="Master_Rooftop_Dataset/test/images", # Path to predicted images
        conf=0.25,      # Confidence threshold 
        save=True,      # Saves images with boxes drawn on them (for you to see)
        save_txt=True, 
        imgsz=640       # Matching the resoluation of the training
    )
    
    print("Inference complete. Check  for your new labels!")

if __name__ == '__main__':
    run_inference()