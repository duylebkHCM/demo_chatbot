import os
import sys

# insert path of this script in syspath so run_nlu_server.py will be found
sys.path.insert(1, os.path.dirname(os.path.abspath(__file__)))

# This is exactly like issuing the command:
#rasa run --enable-api -m models/nlu-20190515-144445.tar.gz

def train_model(data = 'data/', config_path = 'config/config_1.yml', model_dir = 'models/', modules = 'pipeline1'):
    sys.argv.append('train')

    sys.argv.append('-c')

    sys.argv.append(config_path)

    sys.argv.append('--out')

    sys.argv.append(model_dir)

    sys.argv.append('--fixed-model-name')

    sys.argv.append(modules)

    from rasa.__main__ import main
    main()

if __name__ == '__main__':
    train_model()