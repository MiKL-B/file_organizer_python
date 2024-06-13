import os

desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 

ext_images = [".jpg",".jpeg",".bmp",".png",".gif"]
ext_documents = [".txt",".pdf"]

def make_dirs(path):
    if not os.path.isdir(path):
        os.makedirs(path)

def organize():
    directory = os.listdir(desktop)
    for filename in directory:
        folder = ""
        for ext in ext_images:
            if ext in filename:
                folder = "My images"
        for ext in ext_documents:
            if ext in filename:
                folder = "My documents"

        make_dirs(desktop + "\\" + folder)
        os.replace(desktop + "\\" + filename, desktop + "\\" + folder + "\\" + filename)

organize()