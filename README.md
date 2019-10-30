# SmartHepSub
## Download
```sh
git clone https://github.com/xxmawhu/SmartHepSub.git
```
## install
```sh
python setup.py install
```
You can also install it into your local directory by
```sh
python setup.py install --user
```
or install it by pip
```sh
pip install SmartHepSub 
```
## Usage
### Setup
* set your own submit style in `~/.SmartHepSubrc`
You can set the number of processor used, and the submit commands
```
[core]
subbashjob = /afs/ihep.ac.cn/soft/common/sysgroup/hep_job/bin/hep_sub -g physics
subbossjob = /afs/ihep.ac.cn/soft/common/sysgroup/hep_job/bin/boss.condor
num_processor = 20
```
### Two typical uasge
* submit the jobs with type `.sh` in one directory `jobs`
```
hep.sub  -sh jobs [-r]
or hep.sh -c jobs [-r]
```
* submit files with `*`
```
hep.sub jobs/*.sh
```
## Help
```
hep.sub -h
```
