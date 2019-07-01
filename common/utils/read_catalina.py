import os

class Read_Catalina(object):
    def read_catalina(self,logName):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = base_dir + '\\log\\{}'.format(logName)
        log_info = open(file_path,'r',encoding='utf-8')
        return log_info

    def get_open_id(self,line):
        r = []
        for i in range(len(line)):
            if line[i].__contains__('uid'):
                r.append(line[i])
                str = ''.join(r)
                par = str.partition("uid=")
                open_id = ""
                for c in par[2]:
                    if c in (
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                    "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"):
                        open_id += c
                    else:
                        if c == ":" or c == " ":
                            if open_id == "":
                                continue
                        break
        return open_id
