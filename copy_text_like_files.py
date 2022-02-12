 

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

if not os.path.exists(args.output):
    os.makedirs(args.output)
# print(args.output)
if not args.data_path.endswith('/'):
   args.data_path += '/'

# make folders first
for item in glob.glob(args.data_path+'**',recursive=True):
    # print(item.replace(args.data_path,''))
    relative_item = item.replace(args.data_path,'')
    if os.path.isdir(item):
        make_dir_path = join(args.output,relative_item)
        # print(make_dir_path)
        if not os.path.exists(make_dir_path):
            os.makedirs(make_dir_path)
            pass 
# copy text-like files
for item in glob.glob(args.data_path+'**',recursive=True):
    if os.path.isfile(item):
        relative_item = item.replace(args.data_path,'')
        file_type =  f.from_file(item)
        # print(item,file_type)
        if file_type.split('/')[0] == 'text':
            relative_item = item.replace(args.data_path,'')
            new_path = join(args.output,relative_item)
            # print(item)
            shutil.copyfile(item, new_path)
    # print(join(args.data_path,root))
    # print(join(args.output,root))
    # if not os.path.exists( join(args.output,root)):
        # os.makedirs(join(args.output,root))
    # for name in files:
        # full_name = os.path.join(root, name)
        # # print(full_name , os.path.isdir(full_name) )
        # (base, ext) = os.path.splitext(name) # split base and extension
        # if ext in ('.jpg', '.gif'):          # check the extension
            # count += 1
            # full_name = os.path.join(root, name) # create full path
            # # print(full_name)


