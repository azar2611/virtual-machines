# virtual-machines

Python utility to list, start, stop, modify and add virtual machines.

## Prerequisite
1. Installed python3
2. Updated pip
3. Installed venv

## How to Install
1. `python3 -m venv /path/to/new/virtual/environment For e.g python3 -m venv python3-venv`
2. `source /path/to/new/virtual/environment/bin/activate For e.g source python3-venv/bin/activate`
3. `git clone https://github.com/azar2611/virtual-machines.git`
4. `cd virtual-machines`
5. `pip install .`
6. `vm --help`

## Examples/Testcases
1. `vm list` List all virtuall machines.
2. `vm list --running=yes` List Only running virtual machines. 
3. `vm list --stopped=yes` List Only stopped virtual machines.
4. `vm add -t type01.core -n instance16 -im img-12345678925 -i i-12345678925 -ip 10.10.10.25` Add instance with InstanceId=i-12345678915 check with `vm list`
5. `vm stop -i i-12345678910` Stopped running instance check with `vm list stopped=yes`
6. `vm start -t type02.core -o ubuntu` Start stopped instance check with `vm list running=yes`
7. `vm modify -t type03.core -i i-12345678910` check with `vm list`


