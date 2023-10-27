import re
import platform
import base64
from hashlib import md5 as _md5
import binascii

def to_base64(data_bytes):
    encoded_data = base64.b64encode(data_bytes)
    return encoded_data.decode('utf-8')

def to_hex(data_bytes):
    hex_encoded = binascii.hexlify(data_bytes)
    return hex_encoded.decode('utf-8')

def require(module):
    index = 0
    module_array = module.split('.')
    for m in module_array:
        if index == 0:
            _module = __import__(m)
            index += 1
        else:
            _module = getattr(_module, m)
            index += 1
    return _module

def sanitize_filename(filename):
    if platform.system() == 'Windows' or platform.system() == 'Cygwin':
        # Windows不合法文件名字符
        illegal_chars = r'[<>:"/\\|?*\x00-\x1f]'
    else:
        # 不合法文件名字符
        illegal_chars = r'[/\x00-\x1f]'
    # 将不合法字符替换为下划线
    return re.sub(illegal_chars, '_', filename)

def md5(s: str):
    # 计算md5
    return _md5(s.encode("utf-8")).hexdigest()

def readfile(path, mode = "text"):
    try:
        fileObj = open(path, "rb")
    except FileNotFoundError:
        return "file not found"
    content = fileObj.read()
    if mode == "base64":
        return to_base64(content)
    elif mode == "hex":
        return to_hex(content)
    elif mode == "text":
        return content.decode("utf-8")
    else:
        return "unsupported mode"

def unique_list(list_in):
    unique_list = []
    [unique_list.append(x) for x in list_in if x not in unique_list]
    return unique_list
