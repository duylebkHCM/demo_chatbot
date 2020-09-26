import yaml
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader

def get_domain():
    domain_file = open("domain.yml")
    domain = yaml.load(domain_file,Loader=yaml.FullLoader)
    return domain

def fill_template():
    domain = get_domain()
    env = Environment(loader = FileSystemLoader('./action_templates'),   trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('template.py')
    actions = template.render(domain)
    return actions

def generate_file(filepath):
    with open(filepath,'wt') as file:
        file.write(fill_template())
    

if __name__== "__main__" :
    generate_file("./actions.py")


