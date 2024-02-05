import coremltools
import tensorflow as tf

model_path = '/Users/adityaghai/Desktop/Clock_drawing/CNN/CNN 4000/model.h5'

keras_model =  tf.keras.models.load_model(model_path)

model = coremltools.convert(keras_model, convert_to="mlprogram")

model.save("CDT_MODEL_CML")
print('conversion done')