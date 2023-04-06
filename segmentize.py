# parse a binary file which consists of segments, each segment starts with a 4 byte header which 
# contains the origin address of the segment and the length of the segment in bytes.

import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='Parse a binary file which consists of segments, each segment starts with a 4 byte header which contains the origin address of the segment and the length of the segment in bytes.')
    parser.add_argument('file', help='binary file to parse')

    args = parser.parse_args()

    f = open(args.file, 'rb')
    data = f.read()
    f.close()
    cumulative_offset =0
    segment,offset = read_segment(data, 0)
    while len(data[cumulative_offset+offset:]) >0:
        cumulative_offset += offset
        segment,offset = read_segment(data[cumulative_offset:], 0)
    

def read_segment(sdata, offset):
    # read the segment header
    header = sdata[offset:offset+4]
    
    offset += 4
    origin = (header[0] | (header[1]<<8) )
    print("origin: %04X" % origin )

    length = int(header[2]  | (header[3]<<8) )
    print("length: %04X" % length )
    segment = sdata[offset:offset+length]
    offset += length
    return (segment, offset)


if __name__ == '__main__':
    main()







