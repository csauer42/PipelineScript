import os
import yaml
from pathlib import Path

parent = Path().parent
fname = os.path.join(parent, 'dependencies/deps.yml')

with open(fname, 'r') as stream:
    deps = yaml.safe_load(stream)

for dep in deps['dependencies']:
    print('%-8s - %6s' % (dep['name'], dep['version']))