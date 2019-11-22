import ctypes
import time
import cv2
import os
import sys

def create_frames(video, frames):
    if video.isOpened() == False:
        print("Error opening video.")
        input()
        return False

    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = video.get(cv2.CAP_PROP_FPS)

    if frames == None or frames == "":
        frames = total_frames
    elif frames > total_frames:
        print("The amount of frames needs to be less than the total amount in the video.")
        input()
        return False

    success, image = video.read()
    for i in range(frames):
        cv2.imwrite(f"frames/frame{i+1}.jpg", image)
        success, image = video.read()
        sys.stdout.write(f"\r{int((i+1)/frames*100)}% complete")
        sys.stdout.flush()

    print("")

def create_folder():
    if not os.path.exists(f"{os.getcwd()}/frames"):
        os.makedirs(f"{os.getcwd()}/frames")

def main():
    path = input("Enter the path of the video: ")
    video = cv2.VideoCapture(path)

    while True:
        try:
            frames = input("Enter the number of frames you want shown (leave blank if you want the entire video): ")
            if frames != "":
                frames = int(frames)
            break
        except:
            print("That isn't a valid number!")
            
    create_folder()

    os.system("cls")
    create_frames(video, frames)

if __name__ == "__main__":
    main()
