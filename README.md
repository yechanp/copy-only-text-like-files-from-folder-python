# copy-only-text-like-files-from-folder-python
copy only text-like files from the folder

This project is for those who want to copy only source code or text files from a folder, not heavy files such as images or videos.

# Prerequisites
This project requires python-magic package. Please install python-magic
```
pip install python-magic
```
# Usage
Please run the code as follows:
```
python copy_text_like_files.py --data_path [FOLDER_TO_BE_COPIED] --output [OUTPUT_DIR]
```

for example, 
```
python copy_text_like_files.py --data_path /home/user1/codes --output ./copied
```
