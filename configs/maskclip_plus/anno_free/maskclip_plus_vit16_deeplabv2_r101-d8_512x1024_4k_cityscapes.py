_base_ = [
    '../../_base_/models/maskclip_plus_vit16.py', '../../_base_/datasets/cityscapes.py', 
    '../../_base_/default_runtime.py', '../../_base_/schedules/schedule_4k.py'
]

suppress_labels = list(range(0, 19))
model = dict(
    decode_head=dict(
        num_classes=19,
        text_categories=19,
        text_embeddings_path='pretrain/city_ViT16_clip_text.pth',
        clip_unlabeled_cats=suppress_labels,
        # num_vote=1,
        # vote_thresh=1.0,
        # cls_thresh=0.5,
        # conf_thresh = 0.1,
    ),
)

find_unused_parameters=True
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
crop_size = (512, 1024)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', suppress_labels=suppress_labels),
    dict(type='Resize', img_scale=(2048, 1024), ratio_range=(0.5, 2.0)),
    dict(type='RandomCrop', crop_size=crop_size, cat_max_ratio=0.75),
    dict(type='RandomFlip', prob=0.5),
    dict(type='PhotoMetricDistortion'),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size=crop_size, pad_val=0, seg_pad_val=255),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_semantic_seg']),
]
data = dict(
    samples_per_gpu=4,
    train=dict(
        pipeline=train_pipeline
    )
)