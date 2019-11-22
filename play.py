import os
import ctypes
import time

def play(fps=30):
    print("Playing!")
    total_frames = len(os.listdir(f"{os.getcwd()}/frames"))
    current_frame = 1
    
    while True:
        if current_frame != total_frames:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{os.getcwd()}/frames/frame{current_frame}.jpg", 0)
            time.sleep(1/fps)
            current_frame += 1
        else:
            current_frame = 0    

if __name__ == "__main__":
    play()
