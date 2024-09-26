import sys
from collect_static.collect import collect_files


def test():
    collect_files(".py")
    

if __name__ == '__main__':
    sys.exit(test())