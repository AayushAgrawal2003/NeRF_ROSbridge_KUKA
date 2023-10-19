
# TODO:
- [X] Make a bridge to convert data from camera position in iiwa to NeRF format
    - [X] Convert camera position data to transformation 
    - [-] Calculate the blur value for the images
    - [X] Generate the JSON file
    - [X] Capture frames from camera 
- [ ] Generate sample data for the rosbag
- [ ] Train a model that can use this generated data
- [X] Write the bridge to transfer data to the NeRF model 
- [ ] Test model output in rviz(Scale and Surface area) 
- [ ] Automate the path planning for automated data collection 

## Generated data

Data captutred form the rosbag can be found in captured frames and its corresponding json can be found in test/test.json