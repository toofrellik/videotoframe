import cv2
import sys
import os
from tqdm import tqdm

sys.path.append("./../")
from configs import main_config
from modules.fetch_data import read_data

video_path = main_config.input_dir

def get_frames(video_path):
  for filename in tqdm(os.listdir(video_path)):
    file_path = video_path+filename
    vidcap = read_data.get_videos(file_path)
    success, image = vidcap.read()
    count = 0
    while success:
      os.chdir(main_config.output_dir)
      if not os.path.exists(filename):
        os.makedirs(filename)
      os.chdir(main_config.output_dir+filename+"/")
      cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
      success,image = vidcap.read()
      count += 1

if __name__ == '__main__':
    get_frames(video_path)