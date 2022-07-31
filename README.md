# virtual-machines

Python utility to list, start, stop, modify and add virtual machines.

## Prerequisite
1. Installed python3
2. Updated pip
3. Installed vene

## How to Install
1. `python3 -m vene /path/to/new/vietual/environment For e.g python3 -m venev python3-vene`
2. `source /path/to/new/vietual/environment/bin/activate For e.g source python3-vene/bin/activate`
3. `git clone https://github.com/azar2611/virtual-machines.git`
4. `cd virtual-machines`
5. `pip install .`
6. `vm --help`

## Examples/Testcases
1. `vm list` List all virtuall machines.
2. `vm list --running=yes` List Only running virtual machines. 
3. `vm list --stopped=yes` List Only stopped virtual machines.
4. `vm add -t type01.core -n instance16 -im img-12345678915 -i i-12345678915 -ip 10.10.10.15` Add instance with InstanceId=i-12345678915


