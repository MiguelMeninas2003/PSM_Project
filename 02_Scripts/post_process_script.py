import os

def clip_labels(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process every .txt file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            with open(input_path, 'r') as f:
                lines = f.readlines()

            cleaned_lines = []
            for line in lines:
                parts = line.split()
                if not parts:
                    continue
                
                # The first part is the Class ID (e.g., 0)
                class_id = parts[0]
                
                # The rest are the coordinates (x1, y1, x2, y2...)
                coords = parts[1:]
                
                # Clip each coordinate between 0.0 and 1.0
                clipped_coords = []
                for c in coords:
                    val = float(c)
                    if val < 0.0:
                        val = 0.0
                    elif val > 1.0:
                        val = 1.0
                    clipped_coords.append(f"{val:.6f}")
                
                # Combine them back into a single line
                new_line = f"{class_id} " + " ".join(clipped_coords)
                cleaned_lines.append(new_line)

            # Save the fixed file
            with open(output_path, 'w') as f:
                f.write("\n".join(cleaned_lines))

    print(f"Done! Cleaned files are in: {output_folder}")

# --- SET YOUR PATHS HERE ---
input_dir = "runs/obb/predict/labels"  
output_dir = "runs/obb/predict/clamped_labels" # New clamped labels

clip_labels(input_dir, output_dir)