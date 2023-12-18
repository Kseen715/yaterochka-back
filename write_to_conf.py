# Write content like this from parameters of command line into file:
# NAME=postgres
# HOST=localhost
# PORT=5432
# PASSWORD=root
# USER=postgres

import os
import sys

if __name__ == '__main__':
    params = sys.argv[1:]
    try:
        # remove file if exists
        os.remove('db.conf')
    except:
        pass
    with open('db.conf', 'w') as f:
        f.write('\n'.join(params))
