"""
Модуль subprocess
"""

import chardet   # необходима предварительная инсталляция: pip install chardet
import subprocess
import platform


param = '-n' if platform.system().lower() == 'windows' else '-c'
args = ['ping', param, '2', 'yandex.ru']
process = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in process.stdout:
    result = chardet.detect(line)
    print('result = ', result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))


# =====================================================
# # определение кодировки системы по умолчанию
import locale
default_encoding = locale.getpreferredencoding()
print(default_encoding)
