## Execute files in pwd
- Settings > Search "python.terminal.executeInFileDir" > Toggle check mark

## Facial Recognition Algorithm 

- As a general idea, the dictionary data structure was used incessantly to track the image name and data linked to the image. The dictionary is thus my favorite python data structure.
- For each image in zip:
    - Given a zip, make a pil object (Important because for efficiency images are not extracted). 
    - Make a pil object dictionary with each image name as the key. 
    - Make a text dictionary with the same key as above.
    - Make a face front bounding box coordinates dictionary with the same key as above.
    - Crop images from the pil object based on bounding box coordinates
    - Downsample faces into thumbnails (if faces are present)
    - Make algorithm to search for the keyword and get faces from images were the keyword is found.

## What is Anti-Aliasing

- Visual errors and artifacts obtained from image rendering is referred to as aliasing.
- Anti-Aliasing seeks to get the proper location of image data in order to have better approximation and topography of image data.
- Approximation of image data using interpolation. Pixels are noisier than vectors hence the need for interpolation.
- Shrinking or downsampling image data (thumbnails) does not suffer much from aliasing.
- Enlarging or upsampling image data (posters) is vulnerable to artifacts from aliasing. Could be called the bootstrap effect (just linked the two worlds).

## Facial Algorithm Workflow

![Dark](face_detection.drawio.png)
![Light](face_detection.drawio_l.png)

## Classes Algorithm?

- The timer class algorithm is a good one and works here because attributes are determined by me and called from a module within the function.

- This procedure works because the user need not know the attributes involved.

- OOP in python is very interesting and except through proper experimentation can you determine the proper algorithm when developing a class.

## OpenCV Algorithm?

- The opencv draw proc is as follows:
    - cv imread reads the image in as an array.
    - For classification:
        - change to grayscale image.
        - Use haar classification to classify and make face rectangles or squares.
        - draw the rectangle(s).

- The opencv crop proc is as follows:
    - cv imread reads the image in as an array.
    - Alternatively read as pil object and convert to np array.
    - For classification:
        - change to grayscale image.
        - Use haar classification to classify and make face rectangles or squares.
        - Convert back to pil object.
        - Crop the pil image.

### CV Classifiers
haarcascade_eye_tree_eyeglasses.xml   haarcascade_mcs_leftear.xml
haarcascade_eye.xml                   haarcascade_mcs_lefteye.xml
haarcascade_frontalface_alt2.xml      haarcascade_mcs_mouth.xml
haarcascade_frontalface_alt_tree.xml  haarcascade_mcs_nose.xml
haarcascade_frontalface_alt.xml       haarcascade_mcs_rightear.xml
haarcascade_frontalface_default.xml   haarcascade_mcs_righteye.xml
haarcascade_fullbody.xml              haarcascade_mcs_upperbody.xml
haarcascade_lefteye_2splits.xml       haarcascade_profileface.xml
haarcascade_lowerbody.xml             haarcascade_righteye_2splits.xml
haarcascade_mcs_eyepair_big.xml       haarcascade_smile.xml
haarcascade_mcs_eyepair_small.xml     haarcascade_upperbody.xml

## Multithreading algorithm?



## References

[Stackoverflow-Find haar-cascades xml file](https://github.com/user/repo/blob/branch/other_file.md)

[Cat facial recognition example](https://machinelearningmastery.com/opencv_object_detection/)

[OpenCV procedure Geeks for Geeks](https://www.geeksforgeeks.org/face-detection-using-cascade-classifier-using-opencv-python/)

[Haar classifier github](https://github.com/opencv/opencv/blob/4.x/data/haarcascades/haarcascade_frontalface_default.xml)

[Drawio](https://github.com/jgraph/drawio-desktop/releases/tag/v24.2.5)

[Tesseract cmd Geeks for Geeks](https://www.geeksforgeeks.org/reading-text-from-the-image-using-tesseract/#)

[Python path validation](https://kodify.net/python/os-path-exist-function/)


