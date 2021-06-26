import tensorflow as tf
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.utils import config_util
from object_detection.builders import model_builder


category_index = label_map_util.create_category_index_from_labelmap(r'./labelmap/label_map.pbtxt', use_display_name=True)
category_index

def get_model():
    """
    pipeline.config 와 checkpooint weight를 이용해 학습된 모델 load
    """
    #pipeline.config를 이용해 config객체 조회
    configs = config_util.get_configs_from_pipeline_file(r'model\pipeline.config') 

    # config의 model 속성을 이용해 detection 모델 객체 생성
    detection_model = model_builder.build(model_config = configs['model'], is_training=False) 
    ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)  #모델의 checkpoint weight 조회
    ckpt.restore(r'model\checkpoint\ckpt-21').expect_partial() 
    return detection_model


def detect_func(image, detection_model):
    """
    image와 모델을 받아서 추론후 결과를 반환
    1. preprocesing
    2. 추론
    3. 추론결과 postprocessing
    4. 3의 결과 반환
    
    """
    image, shapes = detection_model.preprocess(image) # 이미지 리사이징
    predict_dict = detection_model.predict(image, shapes)
    result = detection_model.postprocess(predict_dict, shapes) # prediction tensors to final detections
    return result

def main():
    model = get_model()
    url = 'http://192.168.0.38:9999/?action=stream'
    # cap = cv2.VideoCapture(url+'/?action=stream')
    cap = cv2.VideoCapture(url)
    if not cap.isOpened():
        sys.exit(1)
    while True:
        ret, img = cap.read()
        if ret:
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            input_tensor = tf.convert_to_tensor(np.expand_dims(img_rgb, 0), dtype=tf.float32) 
            post_detections = detect_func(input_tensor, model)
            
            num_detections = int(post_detections.pop('num_detections')) 

            # num_detectionss = 100
            # detections 딕셔너리에서 num_detections 개수만큼만 추출해서 새로 생성
            detections = {key: value[0, :num_detections].numpy()
                            for key, value in post_detections.items()}

            # detections를 다시 구성했으므로 num_detections 추가
            detections['num_detections'] = num_detections

            # detection_classes를  int로 변환
            detections['detection_classes'] = detections['detection_classes'].astype(np.int64)


            MIN_CONF_THRESH=0.6  
            
            img = viz_utils.visualize_boxes_and_labels_on_image_array(
                                                img, #추론한 원본 이미지. 여기에 bbox를 친다.
                                                detections['detection_boxes'], # 박스정보
                                                detections['detection_classes'] + 1,  # classes는 0부터 나오는데 labelmap은 1부터 이므로 +1 한다. (labemap의 id 0은 배경(background) 것이어서 1부터 줄 수 있다.)
                                                detections['detection_scores'],  # confidence score
                                                category_index,
                                                use_normalized_coordinates=True,  #좌표 normalize 됬는지 여부 - 0 ~ 1사이 숫자
                                                max_boxes_to_draw=100,  #최대 몇개 박스를 칠 것인지 (기본값 20)
                                                min_score_thresh=MIN_CONF_THRESH,)
            cv2.imshow('frame', img)

            if cv2.waitKey(1) > 0:
                break

    cap.release()
    cv2.destroyAllWindows()    

if __name__ == '__main__':
    main()