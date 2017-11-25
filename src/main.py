import sys
from client import *

from utils.jsonreader import *

def main(argv):

    client = TheaterBot()

    jsonLoader = JsonReader()

    client.run(jsonLoader.getServerKey())
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
