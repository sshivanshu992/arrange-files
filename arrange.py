import os
# without changes any things, any one add more extension at the extension() function.
# make pair of Key and Values add more extensions.

# os.getcwdb() # print current dir
# os.getcwd() # print current dir

def mkdir(folder):
    # if directory doesn't exists then make directory(folder)
    if not os.path.exists(folder): 
        os.makedirs(folder)
  

def move(folder, files):
    for file in files:
        os.replace(file, f"{folder}/{file}")


def extensions():
    # in this program key represent the 'directory_Name', value represent the 'extensions'
    return { 
        "zip"           : ['.zip', '.iso'],
        "image"         : ['.png', '.jpg','.jpeg', '.jfif', '.gif', '.heif', '.bmp', '.webp', '.bpg', '.ico'  ],
        "audio"         : ['.mp3'],
        "media"         : ['.mp4','.flv', '.webm'],
        "document"      : ['.html', '.txt', '.htm', '.pdf'],
        "Win_Office"    : ['.doc', '.docx', '.ppt', '.pptx', '.xlsx', '.xls', '.accdb'],
        "Language"      : ['.py', '.pyc', '.c', '.cpp', '.r', '.java', '.js', '.sql', ],

        }

# category function take the plunge (decide), which extension belong to the directory (folders).
def category(files, extension, folder):
        items =  [ file for file in files if os.path.splitext(file)[1].lower() in extension]
        # here items represent the pairs of extensions list or empty list
        move(folder, items)
        # check directory is empty then remove the directory
        #if len(os.listdir(folder)) == 0:
        if not os.listdir(folder): 
            os.rmdir(folder) 

def Main():
    Allfiles = os.listdir()
    Allfiles.remove('arrange.py') 

    extension = extensions()
    for folder in extension.keys():
        mkdir(folder)
        extensionlist = extension[folder] # here folder represent the key of Dictionary 
        category(Allfiles, extensionlist, folder)


if __name__ == '__main__':
    Main()
