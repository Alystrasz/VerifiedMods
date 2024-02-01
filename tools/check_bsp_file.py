import bsp_tool
import sys

def check_bsp_file(path):
    # TODO check file extension
    bsp = bsp_tool.load_bsp(path)
    # print(bsp.headers)
    # TODO check if headers have PAKFILE member
    print(bsp.headers['PAKFILE'])
    # TODO check if header length is 0
    print(len(bsp.headers['PAKFILE'].as_bytes()))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        check_bsp_file(sys.argv[1])
    else:
        print("Expected format:\n\tpython path/to/check_bsp_file.py path/to/file")