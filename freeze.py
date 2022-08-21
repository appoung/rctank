# freeze.py
from tensorflow import keras
model = keras.models.load_model("keras_model.h5", compile=False)

export_path = ''
model.save(export_path, save_format="tf")
#[출처] Keras 모델을 TensorFlow Lite로 변환하기 (h5 -> pb -> tflite)|작성자 aainy