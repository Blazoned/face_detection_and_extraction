# Face Detection & Extraction
Detect face in images in the selected input folders and extract 48x48 images of each detected face on the images in the selected output.

## Usage
You can manually use the terminal or (if you're using Windows) execute the batch file.
### Terminal
Open the folder containing main.py in the terminal. Then execute the command:
```cmd
python main.py "{input_folder_1}:{output_folder_1}" ["{input_folder_2}:{output_folder_2}" ...]
```

### Batch file
Create a virtual python environment in the same folder as main.py. The folder containing the virtual environment must be called `.venv`. The batch file activates this python environment and uses it to transform the seven folders in the input folder to the same folders in the output folder.

The batch file may be changed by editing the python command in accordance with the terminal use case.