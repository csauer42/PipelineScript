import os
import yaml
import subprocess
from pathlib import Path

def download(pkg, version, location):
    cmd = [ 'az',
            'artifacts',
            'universal',
            'download',
            '--organization', 'https://dev.azure.com/CSCOTesting/',
            '--project', '477fc493-2c12-4877-954a-3040372f2485',
            '--scope', 'project',
            '--feed', 'TestArtifacts',
            '--name', pkg,
            '--version', version,
            '--path', location        
          ]
    subprocess.run(cmd)

dldir = 'dependencies'

parent = Path().parent
fname = os.path.join(parent, '.azure/download.yml')

with open(fname, 'r') as stream:
    deps = yaml.safe_load(stream)

for dep in deps['parameters'][0]['default']:
    download(dep['pkg'], dep['version'], dldir)