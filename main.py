import os
import sys
import json
from datetime import datetime
from argparse import ArgumentParser

import cv2
from stream import VideoStream
from fps import FPS


parser = ArgumentParser()
parser.add_argument("-c", "--config", help="path to configuration file", required=True)
parser.add_argument("-v", "--verbose", dest='verbose', action="store_true")
parser.set_defaults(verbose=False)

if __name__ == "__main__":
    args = vars(parser.parse_args())

    # Load configuration file
    with open(args['config']) as f:
        config = json.loads(f.read())

    # Instantiate streaming instance
    vs = VideoStream(src=config['stream']['src'],
                    queue_size=config['stream']['queue_size'],
                    resolution=(int(config['stream']['width']), int(config['stream']['height'])),
                    verbose=args['verbose'])

    # metadata of the exporting video
    now = datetime.now()
    dst_dir = now.strftime("%Y-%m-%d")
    filename = now.strftime("%H-%M-%S") + ".mp4"

    # Make sure the exporting directory exist
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)

    # Writer for exporting video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # codec used

    # VideoWriter
    # - @path
    # - @codec
    # - @fps
    # - @resolution
    out = cv2.VideoWriter(os.path.join(dst_dir, filename), fourcc, 30.0,
                        (int(config['stream']['width']), int(config['stream']['height'])))

    # Start streaming
    vs.start()
    fps = FPS()
    fps.start()

    # TODO: Apply object dectection and face recognition here
    while vs.size() or not vs.stopped:
        frame = vs.read()
        out.write(frame)
        cv2.imshow("Streaming", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            vs.stop()

        fps.update()

    # Stop streaming
    fps.stop()
    vs.stop()

    # Release Resource
    out.release()
    cv2.destroyAllWindows()

    print("Elasped time: %s" % str(fps.elapsed()))
    print("Approximate FPS: %s" % str(fps.fps()))
