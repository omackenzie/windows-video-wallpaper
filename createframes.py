import ctypes
import time
import cv2
import os

def create_frames(path):
    video = cv2.VideoCapture(path)
    if video.isOpened() == False:
        print("Error opening video.")
        input()
        return False

    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = video.get(cv2.CAP_PROP_FPS)

    success, image = video.read()
    for i in range(total_frames):
        cv2.imwrite(f"frames/frame{i+1}.jpg", image)
        success, image = video.read()
        print(f"{i+1}/{total_frames} complete")
        os.system("cls")

def main():
    path = input("Enter the path of the video: ")
    create_frames(path)

if __name__ == "__main__":
    if not os.path.exists(f"{os.getcwd()}/frames"):
        os.makedirs(f"{os.getcwd()}/frames")
    main()
