import time
from queue import Queue
from threading import Thread
import cv2

class VideoStream:

    def __init__(self, src=0, queue_size=256, resolution=(500, 500)):
        """Initialize the video stream

        [Arguments]
        - src
            The source of the video. It can be a integer, used as index of
            the webcam on your system. It can be a string, used as either
            the filename or the url of the ip camera.
        - queue_size
            The size of the stream frame buffer
        - resolution
            Transform all frames to this resolution
        """
        self.stream = cv2.VideoCapture(src)
        self.stopped = False
        self.resolution = resolution
        self.frame_queue = Queue(maxsize=queue_size)
        self.thread = Thread(target=self._update, args=())
        self.thread.daemon = True

        if not self.stream.isOpened():
            raise Exception("Fail to connect to video source")

    def start(self):
        """Start streaming"""
        self.thread.start()
        return self

    def stop(self):
        """Stop streaming and release resource"""
        self.stopped = True
        self.thread.join()

    def read(self):
        """Return next frame"""
        return self.frame_queue.get()

    def size(self):
        """Return number of frames in the queue_buffer"""
        return self.frame_queue.qsize()

    def _update(self):
        """Thread to fill the stream frame buffer"""
        while True:
            # stop the thread
            if self.stopped:
                break

            # add new frame if there is room for it in frame_queue
            if not self.frame_queue.full():
                ret, frame = self.stream.read()

                # reach the end of the video stream, stop the thread
                if not ret:
                    self.stopped = True
                    continue

                # Resize frame
                frame = cv2.resize(frame, self.resolution)

                self.frame_queue.put(frame)
            else:
                # wait 10ms for consumer consuming the frames
                time.sleep(0.1)

        self.stream.release()


if __name__ == "__main__":
    vs = VideoStream()

    vs.start()

    while vs.size() or not vs.stopped:
        frame = vs.read()
        cv2.imshow("Test", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            vs.stop()

    cv2.destroyAllWindows()
