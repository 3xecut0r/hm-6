import pathlib
import sys
import os
import shutil


extensions = {
"images":['.jpeg', '.png', '.jpg', '.svg'],
"video":['.avi', '.mp4', '.mov', '.mkv'],
"documents":['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
"music":['.mp3', '.ogg', '.wav', '.amr'],
"archives":['.zip', '.gz', '.tar'],
"others":[]
}


def create_dirs(path):
    for folder in extensions:
        target = path / folder 
        if not target.exists():
            target.mkdir()

def sorter(path):
    all = os.listdir(path)
    lst = []
    for x in all:
        name, ext = os.path.splitext(x)
        name = normalize(name)
        if x in all:
            
            if not os.path.isdir(f"{path}\\{x}"):
                lst.append(x)
                for key, val in extensions.items():

                    if ext in val:
                        os.rename(f"{path}\\{x}", f"{path}\\{key}\\{name}{ext}")
                        lst.remove(x)
    for i in lst:
        os.rename(f"{path}\\{i}", f"{new_path}\\others\\{i}")                                  
        
def normalize(word):
    result=''
    table ={'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v', 'Г': 'G', 'г': 'g', 'Д': 'D', 'д': 'd',
 'Е': 'E', 'е': 'e', 'Ё': 'E', 'ё': 'e', 'Ж': 'J', 'ж': 'j', 'З': 'Z', 'з': 'z', 'И': 'I', 'и': 'i', 'Й': 'J', 'й': 'j', 'К': 'K', 'к': 'k', 'Л': 'L',
 'л': 'l', 'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n', 'О': 'O', 'о': 'o', 'П': 'P', 'п': 'p', 'Р': 'R', 'р': 'r', 'С': 'S', 'с': 's', 'Т': 'T',
 'т': 't', 'У': 'U', 'у': 'u', 'Ф': 'F', 'ф': 'f', 'Х': 'H', 'х': 'h', 'Ц': 'TS', 'ц': 'c', 'Ч': 'CH', 'ч': 'ch', 'Ш': 'SH', 'ш': 'sh',
 'Щ': 'SCH', 'щ': 'sch', 'Ъ': '', 'ъ': '', 'Ы': 'Y', 'ы': 'y', 'Ь': '', 'ь': '', 'Э': 'E', 'э': 'e', 'Ю': 'YU',
 'ю': 'yu', 'Я': 'YA', 'я': 'ya', 'Є': 'JE', 'є': 'je', 'І': 'I', 'і': 'i', 'Ї': 'JI', 'ї': 'ji', 'Ґ': 'G', 'ґ': 'g', '.':'.', '\\':'\\', ':':':',
 'A':'A', 'B':'B', 'C':'C', 'D':'D'}
    for i in word:
        if i not in table.values():
            if i in table.keys():
                result+=table[i]
            elif '0'<=i<='9':
                result+=i
            else:
                result+='_'
        else:
            result+=i
    return result  

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
        
def sub(path):
    pre = []
    for i in os.listdir(path):
        ipath = os.path.join(path, i)
        if os.path.isdir(ipath):
            pre.append(ipath)
            pre.extend(sub(ipath))
    return pre

def delete(path):
    dirs_lst = sub(path)
    dirs_lst.reverse()
    for i in dirs_lst:
        name = i.split('\\')[-1]
        if name not in extensions.keys():
            if len(os.listdir(i))==0:
                os.rmdir(i)

def main():
    try:
        path = pathlib.Path(sys.argv[1])
        global new_path
        new_path = path
        if os.path.isdir(path):
            create_dirs(path)
            sorter(path) 
            files_dirs(path)
            unpack_arch(path)
            delete(path)     
    except:
        print("Path is not directory")  
    
 
if __name__ == "__main__":
    main()
