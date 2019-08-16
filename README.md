# ip-camera

This repo provides a utility class for connecting IP camera and getting the streaming data.

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
python main.py -c configs/template.json
```

## Configuration file
```
{
    "stream": {
        "src": "rtsp://[username]:[password]@[ip address]:554/[path]",
        "queue_size": 1024,
        "height": 1080,
        "width": 1920
    }
}
```
* **src**  
The source of the flie. It can be integer, or string.  
0 -> the index of the webcam in your system  
"filename" -> the video file  
"url" -> the url of the ip camera  
* **queue_size**  
The buffer size for buffering the streaming data  
* **height**  
height of the resolution  
* **width**  
width of the resolution  
