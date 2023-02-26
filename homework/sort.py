from re import compile, finditer
import pathlib as Path
import sys
import os
import shutil

path = input(">>> ")
extensions = {
"images":['.jpeg', '.png', '.jpg', '.svg'],
"video":['.avi', '.mp4', '.mov', '.mkv'],
"documents":['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
"music":['.mp3', '.ogg', '.wav', '.amr'],
"archives":['.zip', '.gz', '.tar'],
"others":[]
}

new_path = path


def create_dirs(path):
    os.mkdir(f"{path}\\images")
    os.mkdir(f"{path}\\video")
    os.mkdir(f"{path}\\documents")
    os.mkdir(f"{path}\\music")
    os.mkdir(f"{path}\\archives")
    os.mkdir(f"{path}\\others")



def sorter(path):
    all = os.listdir(path)
    lst = []
    for x in all:
        name, ext = os.path.splitext(x)
        if x in all:
            
            if not os.path.isdir(f"{path}\\{x}"):
                lst.append(x)
                for key, val in extensions.items():

                    if ext in val:
                        os.rename(f"{path}\\{x}", f"{path}\\{key}\\{name}{ext}")
                        lst.remove(x)
    for i in lst:
        os.rename(f"{path}\\{i}", f"{new_path}\\others\\{i}")                    

          
             
                





 

def normalize(path):
    text = ''
    
    table = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g',
        'д': 'd', 'е': 'e', 'є': 'ie', 'ж': 'zh', 'з': 'z',
        'и': 'y', 'і': 'i', 'ї': 'i', 'й': 'i', 'к': 'k',
        'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
        'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f',
        'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
        'ь': '', 'ю': 'iu', 'я': 'ia', 'А': 'A', 'Б': 'B',
        'В': 'V', 'Г': 'H', 'Ґ': 'G', 'Д': 'D', 'Е': 'E',
        'Є': 'IE', 'Ж': 'ZH', 'З': 'Z', 'И': 'Y', 'І': 'I',
        'Ї': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
        'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S',
        'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TS',
        'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 'Ь': '', 'Ю': 'IU',
        'Я': 'IA', ' ': ' ', '/':'/', '~':'~', 'w':'w', 'c':'c',
        '.':'.', 'x':'x'
    }
    
    
    for i in path:
        if i not in table.values():
            if i in table.keys():
                text+=table[i]
            elif '0'<=i<='9':
                text+=i
            else:
                text+='_'
        else:
            text+=i
            
    return os.rename(f'{path}', f'{text}')
    

def files_dirs(path):
    result = [f.path for f in os.scandir(path) if f.is_dir()]
    for item in result:
        if item.split("\\")[-1] not in extensions.keys():
            files_dirs(item)
            sorter(item)
            
            
def unpack_arch(path):
    way = [i for i in os.listdir(f"{path}\\archives\\")]
    for i in way:
        name = i.split(".")[0]
        os.mkdir(f"{path}\\archives"+f"\\{name}")
        shutil.unpack_archive(f"{path}\\archives\\{i}", f"{path}\\archives\\{name}")
        os.remove(f"{path}\\archives\\{i}")
        
def get_pre(path):
    pre = []
    for i in os.listdir(path):
        ipath = os.path.join(path, i)
        if os.path.isdir(ipath):
            pre.append(ipath)
            pre.extend(get_pre(ipath))
    return pre
def delete(path):
    dirs_lst = get_pre(path)
    dirs_lst.reverse()
    for i in dirs_lst:
        name = i.split('\\')[-1]
        if name not in extensions.keys():
            if len(os.listdir(i))==0:
                os.rmdir(i)
 

# create_dirs(path)
# sorter(path) 
# files_dirs(path)
# unpack_arch(path)
delete(path)



