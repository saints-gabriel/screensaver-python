import os
import sys

SONGS_DIR_NAME = "songs"


def get_songs_dir() -> str:
    if getattr(sys, "frozen", False):
        exe_dir = os.path.dirname(sys.executable)
        external = os.path.join(exe_dir, SONGS_DIR_NAME)
        if os.path.isdir(external):
            return external

        bundle_dir = getattr(sys, "_MEIPASS", None)
        if bundle_dir:
            bundled = os.path.join(bundle_dir, SONGS_DIR_NAME)
            return bundled

        return external
    else:
        here = os.path.dirname(__file__)
        return os.path.join(here, SONGS_DIR_NAME)
