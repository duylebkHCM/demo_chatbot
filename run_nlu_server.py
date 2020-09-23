import os
import sys

# insert path of this script in syspath so run_nlu_server.py will be found
sys.path.insert(1, os.path.dirname(os.path.abspath(__file__)))

# This is exactly like issuing the command:
#rasa run --enable-api -m models/nlu-20190515-144445.tar.gz

def run_nlu(model_path = 'models/pipeline1/pipeline1.tar.gz'):
    sys.argv.append('run')

    sys.argv.append('--enable-api')

    sys.argv.append('-m')

    sys.argv.append(model_path)

    sys.argv.append('--cors')

    sys.argv.append('"*"')

    sys.argv.append('--debug')

    from rasa.__main__ import main
    main()

if __name__ == '__main__':
    run_nlu()