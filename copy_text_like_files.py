#json yaml config cfg yml 

import magic
import argparse
import os,sys
import shutil
import glob 
parser = argparse.ArgumentParser()
parser.add_argument("--data_path",type=str, default="/data/data/",help='path to dir')
parser.add_argument("--output",type=str, default="/data/copied/",help='path to dir')
args = parser.parse_args()

join = os.path.join
f = magic.Magic(mime=True, uncompress=True)

ALLOW_LIST= []   # e.g. ['.mat']
DENY_LIST = []   # e.g. ['.csv' ,'.md'] 
ONLY_NAME_LIST = ['.pth']

def check_text_like(item,f):
    file_type =  f.from_file(item)
    if file_type.split('/')[0] == 'text':
        return True
    else:
        return False
if not os.path.exists(args.output):
    os.makedirs(args.output)
if not args.data_path.endswith('/'):
   args.data_path += '/'

# make folders first
for item in glob.glob(args.data_path+'**',recursive=True):
    relative_item = item.replace(args.data_path,'')
    if os.path.isdir(item):
        make_dir_path = join(args.output,relative_item)
        if not os.path.exists(make_dir_path):
            os.makedirs(make_dir_path)
            pass 
# copy text-like files
all= glob.glob(args.data_path+'**',recursive=True)
for idx,item in enumerate( all):
    if idx%100 == 0 :
        print('idx',idx,'/', len(all))
    if os.path.isfile(item):
        _,ext = os.path.splitext(item)
        if ext in DENY_LIST:
            continue
        if ext in ALLOW_LIST or check_text_like(item,f):
            relative_item = item.replace(args.data_path,'')
            new_path = join(args.output,relative_item)
            shutil.copyfile(item, new_path)
        elif ext in ONLY_NAME_LIST:
            relative_item = item.replace(args.data_path,'')
            new_path = join(args.output,relative_item)
            if not os.path.isfile(new_path):
                os.mknod(new_path)
