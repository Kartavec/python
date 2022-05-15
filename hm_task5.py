import chardet
import subprocess
import platform

if __name__ == "__main__":
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    args = [['ping', param, '2', 'yandex.ru'], ['ping', param, '2', 'youtube.com']]
    process = subprocess.Popen(args[0], stdout=subprocess.PIPE)
    for line in process.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))
    process = subprocess.Popen(args[1], stdout=subprocess.PIPE)
    for line in process.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))
