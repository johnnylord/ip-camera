from datetime import datetime

class FPS:

    def __init__(self):
        self._start = None
        self._end = None
        self._numFrames = 0

    def start(self):
        """Start the timer"""
        self._start = datetime.now()
        return self

    def stop(self):
        """Stop the timer"""
        self._end = datetime.now()

    def update(self):
        """Increase the frames in the session"""
        self._numFrames += 1

    def elapsed(self):
        """Return the elapsed time"""
        return (self._end - self._start).total_seconds()

    def fps(self):
        """Compute the (approximiate) frames per second"""
        return self._numFrames / self.elapsed()
