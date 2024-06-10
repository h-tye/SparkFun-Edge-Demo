#convert .tflite to cc file and make neccessary adjustments
#add this to end of your trained tflite model

model_all_path = "final_model.tflite"

!apt-get -qq install xxd

!xxd -i {model_all_path} > {model_cc_path}

model_cc_path = "model.cc"

# This is needed to make our model compatible with the infastructure(hello_world directory) already in place
REPLACE_TEXT = model_all_path.replace('/', '_').replace('.', '_')
!sed -i 's/'{REPLACE_TEXT}'/g_model/g' {model_cc_path}
