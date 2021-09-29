import os
import yaml
from pathlib import Path

parent = Path().parent
fname = os.path.join(parent, '.azure/dependencies.yml')

with open(fname, 'r') as stream:
    deps = yaml.safe_load(stream)

for dep in deps['parameters'][0]['default']:
    print('%-10s - %s' % (dep['pkg'], dep['version']))