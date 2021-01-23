import json
import math
import argparse


def parse_args():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Script for sequence file for ffmpeg image concatenation.')
    parser.add_argument("--imageset", required=True, ## lisa, comic
                        metavar="IAMGESET", 
                        help="Image set id")
    parser.add_argument("--input", required=True,
                        metavar="INPUT",
                        help="lips sync input file")
    parser.add_argument("--output", required=True,
                        metavar="OUTPUT",
                        help="sequence file")
    args = parser.parse_args()

    return args.imageset , args.input , args.output

imageset , inputFile , outputFile = parse_args()

sequence = ["#filelist"]

with open(inputFile) as json_file:
    data = json.load(json_file)
    for p in data['mouthCues']:
        frames = round(100 * (p['end'] - p['start']))
        print(p['start'],p['end'],p['value'],frames);
        sequence.append("#start={0} end={1} {2} x {3}".format(p['start'],p['end'],frames,p['value']));
        for _ in range(frames):
            sequence.append("file 'img/{0}-{1}.png'".format(imageset,p['value']))
            sequence.append("duration {0}".format(0.01))



print("Create",outputFile)
with open(outputFile, 'w') as f:
    for item in sequence:
        f.write("%s\n" % item)