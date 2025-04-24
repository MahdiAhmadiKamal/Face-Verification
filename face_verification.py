import argparse
import numpy as np
import cv2
from insightface.app import FaceAnalysis


parser = argparse.ArgumentParser()
parser.add_argument('--image1', type=str, default="input\img1.jpg")
parser.add_argument('--image2', type=str, default="input\img2.jpg")

opt = parser.parse_args()

app = FaceAnalysis(name="buffalo_s", providers=['CUDAExecutionProvider'])
app.prepare(ctx_id=0, det_size=(640, 640))

image_1 = cv2.imread(opt.image1)
image_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2RGB)
image_2 = cv2.imread(opt.image2)
image_2 = cv2.cvtColor(image_2, cv2.COLOR_BGR2RGB)

result_1 = app.get(image_1)
result_2 = app.get(image_2)
embedding_1 = result_1[0]["embedding"]
embedding_2 = result_2[0]["embedding"]

diff = np.sqrt(np.sum((embedding_1 - embedding_2)**2))

if diff <= 25:
    print(diff)
    print("\n*Same Person*")

else:
    print(diff)
    print("\n*Different Persons*")