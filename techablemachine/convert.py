import tensorflow as tf

saved_model_dir = 'C:/python/rctank'
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS,
                                       tf.lite.OpsSet.SELECT_TF_OPS]
tflite_model = converter.convert()
open('converted_model.tflite', 'wb').write(tflite_model)
#[출처] Keras 모델을 TensorFlow Lite로 변환하기 (h5 -> pb -> tflite)|작성자 aainy