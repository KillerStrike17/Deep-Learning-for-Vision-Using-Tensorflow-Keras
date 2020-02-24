# Data Annotation

Created a labelled Face Dataset using [VGG Annotator](http://www.robots.ox.ac.uk/~vgg/software/via/). 
The dataset contains the images of people looking in some direction which is Up, Down,Left,Right,Top, Back, UpRight, UpLeft, DownRight and DownLeft.

After Labelling, the centroid of bounding box with and without location is extracted and 4 potencial Anchor Boxes are generated using KMeans Algorithm.


rename_resize.py is the script to rename and resize the images to 400 x 400.

kmeans_with_location.py is used to find the potencial anchor boxes. 

Here, I have calculated k means wth and and without including initial location.

### Annotation Screenshots:

**Up**

![Up Annotated Image](Assets/up.png)

**Down**

![Down Annotated Image](Assets/down.png)

**Left**

![Left Annotated Image](Assets/left.png)

**Right**

![Right Annotated Image](Assets/right.png)

**Top**

![Top Annotated Image](Assets/top.png)

**Back**

![Back Annotated Image](Assets/back.png)

**UpRight**

![UpRight Annotated Image](Assets/upright.png)

**UpLeft**

![UpLeft Annotated Image](Assets/upleft.png)

**DownRight**

![DownRight Annotated Image](Assets/downright.png)

**DownLeft**

![DownLeft Annotated Image](Assets/downleft.png)

### KMeans Results

![Kmeans Without Initial Location](Assets/kmeans.png)

Here the four potencial bounding boxes are decided based just over the size of the box

![Kmeans With Initial Location](Assets/kmeans_with_location.png)

Here the four potencial bounding boxes are decided based over the size of the box and location of the boxes.

[Link to Dataset](https://drive.google.com/drive/folders/1IXQHnZ2I55tlWahcsfY4gIIoJtUcXN3t)

