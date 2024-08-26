import argparse, warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

def transformer_opt(opt):
    opt = vars(opt)
    del opt['data']
    del opt['weight']
    del opt['save_json']
    del opt['rect']
    return opt
    
def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--weight', type=str, default='D:\重做消融实验\yolov8s\yolov8s-p2+Datten+MPDiou+Dysnake+dyhead\weights\\best.pt', help='training model path')
    parser.add_argument('--data', type=str, default='D:\\BaiduNetdiskDownload\\yolov8-main-Ghost\\dataset\\VisDrone.yaml', help='data yaml path')
    # parser.add_argument('--data', type=str, default='D:\\BaiduNetdiskDownload\\yolov8-main-Ghost\\ultralytics\\datasets\\RSOD.yaml', help='data yaml path')
    parser.add_argument('--imgsz', type=int, default=1024, help='size of input images as integer')
    parser.add_argument('--batch', type=int, default=4, help='number of images per batch (-1 for AutoBatch)')
    parser.add_argument('--split', type=str, default='test', choices=['train', 'val', 'test'], help='dataset split to use for validation, i.e. val, test or train')
    parser.add_argument('--project', type=str, default='runs/val', help='project name')
    parser.add_argument('--name', type=str, default='test', help='experiment name (project/name)')
    parser.add_argument('--save_txt', action="store_true", help='save results as .txt file')
    parser.add_argument('--save_json', action="store_true", help='save results to JSON file')
    parser.add_argument('--save_hybrid', action="store_true", help='save hybrid version of labels (labels + additional predictions)')
    parser.add_argument('--conf', type=float, default=0.001, help='object confidence threshold for detection (0.001 in val)')
    parser.add_argument('--iou', type=float, default=0.55, help='intersection over union (IoU) threshold for NMS')
    parser.add_argument('--max_det', type=int, default=300, help='maximum number of detections per image')
    parser.add_argument('--half', action="store_true", help='use half precision (FP16)')
    parser.add_argument('--dnn', action="store_true", help='use OpenCV DNN for ONNX inference')
    parser.add_argument('--plots', action="store_true", default=True, help='ave plots during train/val')
    parser.add_argument('--rect', action="store_true", help='rectangular val')
    
    return parser.parse_known_args()[0]

class YOLOV8(YOLO):
    '''
    weigth:model path
    '''
    def __init__(self, weight='', task=None) -> None:
        super().__init__(weight, task)
        
if __name__ == '__main__':
    opt = parse_opt()
    
    model = YOLOV8(weight=opt.weight)
    model.val(data=opt.data,
              save_json=True, rect=True,
              **transformer_opt(opt),
              )