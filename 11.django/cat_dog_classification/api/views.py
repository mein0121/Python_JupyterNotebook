import os
import json
import numpy as np
from PIL import Image

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from config import settings

from . import forms
# from .models import Person
from .apps import ApiConfig

@csrf_exempt
def predict(request):
    # 1. 요청 파라미터 조회(업로드 이미지 조회) - Form 
    # form에 요청 파라미터를 넣어서 Form객체를 생성
    # request.POST: 요청파라미터, request.FILES: 요청파라미터중 업로드된 파일.
    form = forms.UploadForm(request.POST, request.FILES) 
    # 요청 파라미터 검증중 오류가 없으면.
    if form.is_valid():
        clean_data = form.cleaned_data # (검증 통과한) 요청파라미트들을 딕셔너리 형태로 제공.

        # 업로드된 파일 -> ImageField객체를 반환(업로드된 이미지 파일관련 정보) 일반 요청 파라미터의 경우는 값을 반환.
        img = clean_data['upimg'] 
        # ImageField객체는 아래사항을 반환.
        # img.image.width, img.image.height (이미지의 가로, 세로 크기), img.image.format(이미지 형식-타입-mime type-image/jpg)
        # img.name, img.size: 업로드된 파일명, 파일크기(byte)

    # 2. 모델을 이용해서 추론. 모델을 loading
    # 전처리
    image = Image.open(img) # Pillow.Image(ImageField객체) => 업로드된 이미지 파일을 읽어서 Image객체 생성.
    image_resize = image.resize((150,150)) # cnn모델의 input shape에 맞춰서 resize
    image_arr = np.array(image_resize) # numpy(ndarray) 배열로 변환
    image_arr = image_arr/255. # 0 ~ 1 사이로 정규화.
    input_tensor = image_arr[np.newaxis, ...]  # (h, w, c) => (batch_size, h, w, c)
    
    # 모델을 조회.
    model = ApiConfig.model
    #추론
    pred = model.predict(input_tensor)
    label = np.where(pred[0,0]<0.5, 'CAT', 'DOG')

    # 업로드된 파일을 MEDIA_ROOT 경로에 복사.
    save_path = os.path.join(settings.MEDIA_ROOT, img.name) # media_root/업로드 파일명
    image.save(save_path) # 이미지를 주어진 path에 저장.

    # 응답 데이터 - json형식(추론결과-확률, label, 이미지 url)
    # dict => json문자열: value는 파이썬 타입(ndarray는 변환 못한다.)
    result = {
        "label":str(label),
        "pred":float(pred[0,0]),
        "img_url":f'/media/{img.name}'
    }

    return JsonResponse(result)

