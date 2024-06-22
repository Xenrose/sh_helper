############################################################
### pip import

# python I/O
from pathlib import Path
import json, sys, os, shutil
from tqdm import tqdm
from copy import deepcopy

# 데이터 분석 & 시각화
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# bbox 및 시각화
import cv2
from shapely import Polygon
from PIL import Image, ImageDraw, ImageDraw, ImageFont

# wav / soundfile
import librosa, soundfile

# json view
from collections import OrderedDict
from pprint import pprint 

# ETC
import random
import string


############################################################
### shapely.Polygon
# shapely.Polygon 객체를 통해 중앙값을 출력. (text를 출력하기 위해 사용)
def get_center_point(coordinates:list) -> tuple:
    poly = Polygon(coordinates)
    center = poly.centroid
    return (center.x, center.y)


############################################################
### cv2 imread/imwrite
def imread(filename) -> np.array:
    n = np.fromfile(filename, np.uint8)
    img = cv2.imdecode(n, cv2.IMREAD_COLOR)
    return img
    
def imwrite(filename, img:np.array, params=None):
    ext = os.path.splitext(filename)[1]
    result, n = cv2.imencode(ext, img, params)

    if result:
        with open(filename, mode='w+b') as f:
            n.tofile(f)


############################################################
### IOU calculate
def calculate_iou(polygon1, polygon2):
    intersection = polygon1.intersection(polygon2).area
    union = polygon1.union(polygon2).area
    iou = intersection / union
    return iou

# word의 iou를 계산하여 어떤 div/br에 속하는지 반환해주는 함수
def check_iou(div_info:dict, points:list) -> int:
    # 해당 json에 div 영역이 없는 경우
    if div_info == {}:
        return 0, False
    
    target = Polygon(points).buffer(0)

    iou_list = []
    div_key = []
    for key, div in div_info.items():
        temp_poly = Polygon(div).buffer(0)
        iou = calculate_iou(target, temp_poly)
        iou_list.append(iou)
        div_key.append(key)

    if set(iou_list) == {0.0}: # div에 속하지 않는 word (유령 객체)
        return 0, False
    
    # iou max값이 2 이상이라는 의미는 해당 word는 서로 다른 2개 이상의 div에 덮어 씌워진다는 의미
    log = True if iou_list.count(max(iou_list)) > 1 else False 

    return div_key[iou_list.index(max(iou_list))], log


############################################################
### input/output folder path copy
def create_folder_structure(file_path:Path, output_path:Path, switch_output:Path) -> Path:
    _path = Path(output_path)
    for path in file_path.parts[len(switch_output.parts):]:
        _path = Path(_path, path)
        if not os.path.isdir(_path):
            os.mkdir(_path)

    return _path



