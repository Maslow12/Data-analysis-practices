import os,sys,fnmatch

def import_many_files(extention, dir=None):
    if dir is None: 
        files = fnmatch.filter(os.listdir(os.getcwd()), f'*.{extention}')
    else:
        files = fnmatch.filter(os.listdir(os.path.join(f'{dir}')), f'*.{extention}')
    return files

print(import_many_files('csv'))