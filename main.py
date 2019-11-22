import argparse
import cv2
import createframes
import play

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--path", required=True, help="The path of the video")
    ap.add_argument("-f", "--frames", required=False, type=int, help="The amount of frames you want to play")

    args = vars(ap.parse_args())

    video = cv2.VideoCapture(args["path"])
    fps = video.get(cv2.CAP_PROP_FPS)

    createframes.create_folder()
    createframes.create_frames(video, args["frames"])
    play.play(fps)

if __name__ == "__main__":
    main()
