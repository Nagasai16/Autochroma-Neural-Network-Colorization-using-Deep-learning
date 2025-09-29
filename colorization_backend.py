import numpy as np
import cv2
from pathlib import Path
import os

# Paths to model files
DIR = Path("model")
PROTOTXT = DIR / "colorization_deploy_v2.prototxt"
MODEL = DIR / "colorization_release_v2.caffemodel"
POINTS = DIR / "pts_in_hull.npy"

# Load network
net = cv2.dnn.readNetFromCaffe(str(PROTOTXT), str(MODEL))
pts = np.load(str(POINTS))
pts = pts.transpose().reshape(2, 313, 1, 1)

# Add cluster centers to the model
class8 = net.getLayerId("class8_ab")
conv8 = net.getLayerId("conv8_313_rh")
net.getLayer(class8).blobs = [pts.astype("float32")]
net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]

# Colorization function
def colorize_image(image_path):
    print(f"Colorizing image: {image_path}")
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Could not read image at {image_path}")

    scaled = image.astype("float32") / 255.0
    lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)
    L = lab[:, :, 0]
    L_resized = cv2.resize(L, (224, 224))
    L_resized -= 50

    net.setInput(cv2.dnn.blobFromImage(L_resized))
    ab_decoded = net.forward()[0, :, :, :].transpose((1, 2, 0))
    ab_resized = cv2.resize(ab_decoded, (image.shape[1], image.shape[0]))

    L_original = lab[:, :, 0]
    colorized_lab = np.concatenate((L_original[:, :, np.newaxis], ab_resized), axis=2)
    colorized_bgr = cv2.cvtColor(colorized_lab, cv2.COLOR_LAB2BGR)
    colorized_bgr = np.clip(colorized_bgr, 0, 1)
    colorized_bgr = (colorized_bgr * 255).astype("uint8")

    os.makedirs("static/output", exist_ok=True)
    base = os.path.splitext(os.path.basename(image_path))[0]
    output_path = f'static/output/colorized_{base}.jpg'
    cv2.imwrite(output_path, colorized_bgr)
    print(f"Saved colorized image to: {output_path}")
    return output_path
