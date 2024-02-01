import bsp_tool
import sys

def check_bsp_file(path):
    # TODO check file extension
    bsp = bsp_tool.load_bsp(path)
    # print(bsp.headers)
    # TODO check if headers have PAKFILE member
    print(bsp.headers['PAKFILE'])

    # Check if header length is 0
    header = bsp_tool.branches.respawn.titanfall2.LumpHeader.from_bytes(bsp.headers['PAKFILE'].as_bytes())
    len = header.__dict__['length']
    if len != 0:
        print(f"BSP file \"{path}\" contains scripts, exiting.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        check_bsp_file(sys.argv[1])
    else:
        print("Expected format:\n\tpython path/to/check_bsp_file.py path/to/file")