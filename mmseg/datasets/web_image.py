# Copyright (c) OpenMMLab. All rights reserved.
import os.path as osp

from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class WebImageDataset(CustomDataset):
    def __init__(self, **kwargs):
        data_name = kwargs.pop('data_name', 'batman')
        
        super(WebImageDataset, self).__init__(
            img_suffix='.jpg', seg_map_suffix='.png', **kwargs)
        assert osp.exists(self.img_dir)
        
        if data_name in ['batman', 'gates', 'mickey', 'mario']:
            from tools.denseclip_utils.prompt_engineering import bg_classes
            WebImageDataset.CLASSES = ['obj1', 'obj2'] + bg_classes
            WebImageDataset.PALETTE = [[255, 0, 0], [0, 0, 255]] + [[0, 0, 0]] * len(bg_classes)
        elif data_name == 'blur':
            WebImageDataset.CLASSES = ('blurry car', 'sharp car', 'road',
                            'sidewalk', 'building', 'wall',
                            'fence', 'pole', 'traffic light',
                            'traffic sign', 'vegetation', 'terrain',
                            'sky', 'person', 'rider',
                            'truck', 'bus', 'train',
                            'motorcycle', 'bicycle')
            WebImageDataset.PALETTE = [[255, 0, 0], [0, 0, 255]] + [[0, 0, 0]] * (len(WebImageDataset.CLASSES)-2)
        elif data_name == 'car_brands':
            WebImageDataset.CLASSES = ('Bugatti Veyron', 'Cadillac DeVille',
                        'Porsche 718 Cayman', 'Lamborghini Gallardo'
                        'road', 'sidewalk', 'building', 'wall', 
                        'fence', 'pole', 'traffic light', 'traffic sign', 
                        'vegetation', 'terrain', 'sky', 'person', 'rider', 
                        'truck', 'bus', 'train', 'motorcycle', 'bicycle', 'background')
            WebImageDataset.PALETTE = [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0]] + [[0, 0, 0]] * (len(WebImageDataset.CLASSES)-4)
        elif data_name == 'sports':
            WebImageDataset.CLASSES = ('baseball player', 'basketball player',
                       'soccer player', 'football player',
                       'person', 'background', 'wall', 'building',
                       'sky', 'grass', 'tree', 'ground', 'floor',
                       'baseball court', 'basketball court', 'soccer court', 'football court')
            WebImageDataset.PALETTE = [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0]] + [[0, 0, 0]] * (len(WebImageDataset.CLASSES)-4)