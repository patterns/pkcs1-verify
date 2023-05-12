import hashlib
import os
import sys
import multihash
import multihash.funcs
import multihash.codecs
import multihash.multihash
from multihash import Multihash

def main():
    tarball = os.environ["ARCHIVE_PATH"]
    sha2 = hashlib.sha256()
    with open(tarball, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha2.update(chunk)

    mh = Multihash.from_hash(sha2)
    hex_encoded = mh.encode('hex')
    print(f"::set-output name=sha256::{hex_encoded}")
    sys.exit(0)


if __name__ == "__main__":
    main()
