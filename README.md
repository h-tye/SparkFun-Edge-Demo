# SparkFun-Edge-Demo
A tutorial on the steps necessary to take your own code to the board. Considering the support for this board is far from optimal, I figured someone should provide an outline to work with.
I generated 3 different approaches to flashing binary onto the SparkFun Edge. Only the 1st approach was successful for me but maybe you'll have better luck. 

I was completely unsuccessful with using Arduino with this board but if you can get that to work, it should make this proccess a lot easier. 

#Note
This does not perform inference on the model, it just flashes a model to the board. Currently, I have found that if you use this repo: https://github.com/advaitjain/tflite-micro-sparkfun-edge-examples/tree/main, optimize the main Makefile for size as well as strip debug info then it will create an executable binary that can fit on the board. This should allow you to perform inference on the board but I have not tested it. 







