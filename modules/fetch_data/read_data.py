import os
import sys
import cv2
import glob
sys.path.append("./../")
from configs import main_config

#fetch videos data
def get_videos(path):
  vidcap = cv2.VideoCapture(path)
  return vidcap

def get_videos_count(path):
  len(glob.glob1(path,"*.*"))
