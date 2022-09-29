import logging
import os
import time
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
PathProject = os.path.split(rootPath)[0]
# print(rootPath)
sys.path.append(rootPath)
sys.path.append(PathProject)

from hkws import cm_camera_adpt, config
from example import instant_preview_cb

# 初始化配置文件
cnf = config.Config()
path = os.path.join('../local_config.ini')
cnf.InitConfig(path)

# 初始化SDK适配器
adapter = cm_camera_adpt.CameraAdapter()
userId = adapter.common_start(cnf)
if userId < 0:
    logging.error("初始化Adapter失败")
    os._exit(0)

print("Login successful,the userId is ", userId)

lRealPlayHandle = adapter.start_preview(None, userId)
if lRealPlayHandle < 0:
    adapter.logout(userId)
    adapter.sdk_clean()
    os._exit(2)

print("start preview 成功", lRealPlayHandle)
callback = adapter.callback_standard_data(lRealPlayHandle, instant_preview_cb.f_real_data_call_back, userId)
print("callback", callback)

# deccallback = adapter.callback_Dec(lRealPlayHandle, instant_preview_cb.f_dec_call_back, userId)

time.sleep(36000)
adapter.stop_preview(lRealPlayHandle)
adapter.logout(userId)
adapter.sdk_clean()
