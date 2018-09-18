Code copied from https://github.com/pjreddie/darknet with the following additions:  

`added_scripts/create_txt_data.py`
for creating .txt files for each trainig/test image

`added_scripts/create_data.py`
for creating one .txt-file with path to the training/test images

`cfg/yolo-voc20-fox.cfg`
configuration file for the network.

`cfg/cropped_fox.names`
contains the names for all classes to be trained. Only "fox" for now

`cfg/cropped_fox.data`
contains information on where the training data is located and where to store the weights


### TODOs for training yolo from scratch

<br />

1. `git clone https://github.com/idaswe/darknet`

<br />

2. `cd darknet`

<br />

3. copy images from http://iter.at/yolo-data to `data/logo` so you get this structure: 

`darknet/data/logo/cropped_fox/train` 

`darknet/data/logo/cropped_fox/test` 

`darknet/data/logo/cropped_fox/few-tests` 

The folder few-tests is only used after training to test wheter the network works as expected

<br />

4. YOLOv2 requires one .txt file per image, looking like this: 
`<class> <centerX> <centerY> <width> <height>`  

Make these files: 

`darknet/added_scripts$ python create_txt_data.py` 

You need to run this script twice, one for training and one for test (change from training to test in the file)

<br />

5. YOLO needs to know where the training- and test data is. Generate two files, 

`darknet/cfg/cropped_fox_train.txt` and `darknet/cfg/cropped_fox_test.txt`: 

`darknet/added_scripts$ python create_data.py` 

You'll need to run this script twice, (change train to test in the file) 

<br />

6. Have a look at `cfg/yolo-voc20-fox.cfg` to see how the network is structured. During training, batch should be 64 and subdivision 8, but when testing the network they should both be set to 1. If you're training multiple classes, set filters (line 224) to be (#classes + 5) * 5, and classes (line 230) to be #classes

<br />

7. Have a look at `cfg/cropped_fox.names` and `cfg/cropped_fox.data`

<br />

8. change `exapmles/detector.c` line 138 to save more weights than only each 10.000 batch

<br />

9. Compile darknet: `darknet$ make` (if you're using GPU and CUDNN, change line 1 and 2)

<br />

10. `darknet$ mkdir backup/cropped_fox` (this is the folder we've pointed at in cfg/cropped_fox.data) 

<br />

11. Train the network: `darknet$ ./darknet detector train cfg/cropped_fox.data cfg/yolo-voc20-fox.cfg`

<br />

12. Waiiit 

<br />

13. Test the network: `darknet$ ./darknet detector test cfg/cropped_fox.data cfg/yolo-voc20-fox.cfg <path_to_weights> <path_to_image>` 
