# SparkFun-Edge-Demo
A tutorial on the steps necessary to take your own code to the board. Considering the support for this board has been removed for the most part, this should help out. 
I generated 3 different approaches to flashing binary onto the SparkFun Edge. Only the 1st approach was successful for me but maybe you'll have better luck. 

I was completely unsuccessful with using Arduino with this board but if you can get that to work, it should make this proccess a lot easier. 


This does not perform inference of the model, it just flashes a model to the board. Currently, I have found that if you use this repo: https://github.com/advaitjain/tflite-micro-sparkfun-edge-examples/tree/main, optimize the main Makefile for size as well as strip debug info, then it will create an executable binary that can fit on the board. This should allow you to perform inference on the board but I have not tested it. You then should be able to adjust the source files to create your own projects. You can use your own neural network by following the same steps as approach 3.







