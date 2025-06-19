import os
os.chdir('/Users/yojhu/Desktop/train_plates')
# 設定路徑
base_dir = '/Users/yojhu/Desktop/train_plates'
positive_dir = os.path.join(base_dir, 'positive')
negative_dir = os.path.join(base_dir, 'negative')
info_file = os.path.join(base_dir, 'info.lst')
bg_file = os.path.join(base_dir, 'bg.txt')
vec_file = os.path.join(base_dir, 'output', 'positives.vec')
output_dir = os.path.join(base_dir, 'output')

opencv_createsamples = '/usr/local/bin/opencv_createsamples'
opencv_traincascade = '/usr/local/bin/opencv_traincascade'
# 訓練參數
num_pos = 31
num_neg = 65
width = 72
height = 36
num_stages = 10
feature_type = 'HAAR'  # 或 'LBP'

# 生成 .vec 檔案
def create_samples():
    cmd = f"{opencv_createsamples } -info {info_file} -num {num_pos} -w {width} -h {height} -vec {vec_file}"
    print("Creating .vec file...")
    os.system(cmd)

# 執行訓練
def train_cascade():
    cmd = (
        f"{opencv_traincascade} -data {output_dir} -vec {vec_file} "
        f"-bg {bg_file} -numPos {num_pos} -numNeg {num_neg} "
        f"-numStages {num_stages} -w {width} -h {height} "
        f"-featureType {feature_type}"
    )
    print("Training cascade classifier...")
    os.system(cmd)

if __name__ == '__main__':
    create_samples()
    train_cascade()
