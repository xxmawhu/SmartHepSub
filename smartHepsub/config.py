#!/usr/bin/env python
# encoding: utf-8
# ====================================================
#   Copyright (C)2019 All rights reserved.
#
#   Author        : Xin-Xin MA
#   Email         : xxmawhu@163.com
#   File Name     : config.py
#   Created Time  : 2019-09-19 23:52
#   Last Modified : 2019-10-30 11:03
#   Describe      :
#
# ====================================================
import os
from configparser import ConfigParser
local_config = ConfigParser()
if os.path.exists(os.path.expanduser('~/.SmartHepSubrc')):
    local_config.read(os.path.expanduser('~/.SmartHepSubrc'))
else:
    local_config.add_section('core')
    local_config.set('core', 'subBashJob', 
            "/afs/ihep.ac.cn/soft/common/sysgroup/hep_job/bin/hep_sub -g physics")
    local_config.set('core', 'subBOSSJob', 
            "/afs/ihep.ac.cn/soft/common/sysgroup/hep_job/bin/boss.condor")
    local_config.set('core', 'Num_Processor', "20") 
    with open(os.path.expanduser('~/.SmartHepSubrc'), 'w') as configFile:
        local_config.write(configFile)

user = os.environ["USER"]
if __name__ == "__main__":
    print(local_config['core']['Num_Processor'])
    print(local_config['core']['subBashJob'])
# print local_config.get('core', 'white_file')
