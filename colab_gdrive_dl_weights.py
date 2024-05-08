# Download trained weights for inference on TACO dataset from Github 
# Weights trained on TACO-10 class map, split for 4-fold cross validation
# Unnecessary if you plan to train your own weights

import zipfile
import os
import requests
import shutil

base_url = "https://github.com/pedropro/TACO/releases/download/1.0/taco_10_{}.zip"

for i in range(4):
    url = base_url.format(i)
    filename = f"taco_10_{i}.zip"  # Giving the same name to the file that will be downloaded
    response = requests.get(url)
    
    # Unzip file if it was downloaded successfully
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"File {filename} downloaded successfully.")

        # Path to extract the zip files
        extract_path = '/content/drive/My Drive/Thesis/TACO_repo/'

        for zip_file_path in [filename]:
            # Check if the zip file exists
            if os.path.exists(zip_file_path):
                # Extract the zip file
                with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_path)
                print(f"Extraction of {zip_file_path} completed successfully.")
            else:
                print(f"The specified zip file {zip_file_path} was not found.")
        
        # Move the extracted dataset splits to the data folder
        source_folder = f"/content/drive/My Drive/Thesis/TACO_repo/taco_10_{i}"
        destination_folder = "/content/drive/My Drive/Thesis/TACO_repo/data"
        
        # Iterate over files in source_folder
        for filename in os.listdir(source_folder):
            if filename.endswith(".json"):
                source_file = os.path.join(source_folder, filename)
                destination_file = os.path.join(destination_folder, filename)
                
                try:
                    shutil.move(source_file, destination_file)
                    print(f"Moved {filename} successfully from {source_folder} to {destination_folder}")
                except Exception as e:
                    print(f"Error moving {filename}: {e}")
    else:
        print(f"Failed to download file {filename}. Status code: {response.status_code}")
        break