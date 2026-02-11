from PIL import Image
from pathlib import Path
import os


root = Path(__file__).resolve().parent.parent

input_folder = root / "capturas"
output_folder = root / "capturas"

for filename in os.listdir(input_folder):
    if filename.endswith('.jpg'):
        img = Image.open(os.path.join(input_folder, filename))
        img.save(os.path.join(output_folder, filename.replace('.jpg', '.png')))
        os.remove(os.path.join(output_folder, filename))
    if filename.endswith('.jpeg'):
        img = Image.open(os.path.join(input_folder, filename))
        img.save(os.path.join(output_folder, filename.replace('.jpeg', '.png')))
        os.remove(os.path.join(output_folder, filename))