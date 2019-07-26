# ip-camera

This repo provides a utility class for connecting IP camera and getting the streaming data.

## TODO
- [] synchronize the fps of streaming video and exporting video

## Testing Environment
```
$ uname -a
Linux archlinux 5.2.1-arch1-1-ARCH #1 SMP PREEMPT Sun Jul 14 14:52:52 UTC 2019 x86_64 GNU/Linux
```

## Prerequisites
Here are the third-party python modules used in the project
- opencv-python==4.1.0.25
- numpy==1.16.4

## Run the code
```
python main.py -c configs/webcam.json
```
By default, after executing the program, it will streaming the webcam, display the streaming data through a window, and
save the streaming data as mp4 file with specific filename under specific directory based on current time.

## Configuration file
I have provide a default configuration file `configs/webcam.json`.
```
{
    "stream": {
        "src": 0,           # The source of the flie. It can be integer, or string.
                                # 0 -> the index of the webcam in your system
                                # "filename" -> the video file
                                # "url" -> the url of the ip camera
        "queue_size": 256,  # The buffer size for buffering the streaming data
        "height": 500,      # height of the resolution
        "width": 1000       # width of the resolution
    }
}
```

## How to save/record the streaming data
Please look at `main.py`, and look for `cv2.VideoWriter` part.
