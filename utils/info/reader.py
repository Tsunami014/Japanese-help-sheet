import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

def load_yaml():
    with open("utils/info/data.yml") as f:
        return yaml.load(f, Loader=Loader)
