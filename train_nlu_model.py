from rasa.train import train_nlu
import os

def train_data(data = 'data/nlu.md', config_path = 'config/config_1.yml', model_dir = 'models/', modules = ['pipeline1']):
    for module_name in modules:
        module_directory = os.path.join(model_dir, module_name)
        config_file = config_path
        nlu_data = data

        train_nlu(
            config=config_file,
            nlu_data=nlu_data,
            output=module_directory,
            fixed_model_name=module_name
        )

# if __name__ == '__main__':
#     train_data(data='data/nlu.md', config_path='config/conf
