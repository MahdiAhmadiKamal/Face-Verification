# Face Verification

Face Verification compares two faces taken from photo or video and declares whether they are of the same person or not. A "Same Person" or "Different Persons" determination is made, depending on if the facial features of the faces match or not.

<img src="pics\facial_recognition_freepik_1200.jpg" width="800">

The way it works is that the embedding vectors of images are extracted using [insightface](https://github.com/deepinsight/insightface). Then the vectors are being compared. If the embedding vectors are similar enough, "Same Person" is printed, otherwise "Different Persons" is printed.


## How to install
Run this command:
```
pip install -r requirements.txt
```

## How to run

```
python face_verification.py --image1 PATH/TO/IMAGE1 --image2 PATH/TO/IMAGE2
```