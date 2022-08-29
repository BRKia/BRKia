from typing import *

signDic = {
    "：": ":",
    "，": ",",
    "（": "(",
    "）": ")",
    "【": "[",
    "】": "]",
    "“": "\"",
    "”": "\"",
    "‘": "'",
    "’": "'",
    "；": ";",
    "？": "?",
    "、": "\\",
    "！": "!",
    "￥": "$",
    "小于": "<",
    "大于": ">",
    "的": ".",
}
kwDic = {
    "迭代": "for",
    "返回": "return",
    "在": "in",
    "类": "class",
    "如果": "if",
    "是": "is",
    "导入": "import",
    "定义": "def",
    '结束': 'end',
    '控制台收到数据': 'input',
    '否则': 'else',
    '整数': 'int'
}


def trans(string: str) -> str:
    for k, v in (signDic | kwDic).items():
        string = string.replace(k, v)
    return string