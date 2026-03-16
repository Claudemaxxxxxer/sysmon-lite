import argparse
import time

from . import __version__
from .collect import snapshot


def fmt(s):
    return f"[{s['host']}] cpu {s['cpu']:5.1f}%  mem {s['mem']:5.1f}%  disk {s['disk']:5.1f}%"


def main():
    p = argparse.ArgumentParser(prog="sysmon")
    p.add_argument("--watch", type=int, metavar="SEC", help="refresh interval")
    p.add_argument("--version", action="version", version=__version__)
    args = p.parse_args()

    if not args.watch:
        print(fmt(snapshot()))
        return
    try:
        while True:
            print(fmt(snapshot()))
            time.sleep(args.watch)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
