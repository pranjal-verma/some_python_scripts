import os
from pathlib import Path
#all probable file extensions
dirs = {
    "python": [".py","ipyb"],
    "photos": [".jpg",".jpeg",".png",".svg",".gif"],
    "music":[".mp3",".flac"],
    "go": [".go"] ,
    "docs":[".pdf",".xls",".txt",".doc"],
    "arcs": [".zip",".tar", ".gz", ".rz"],


}

files = {file_format:directory  for directory,file_formats in dirs.items()
        for file_format in file_formats

}

def clean():
    for item in os.scandir():
        if item.is_dir():
            continue
        file_path = Path(item)

        file_format  = file_path.suffix.lower()

        if file_format in files:
            directory_path = Path(files[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))
        for dir in os.scandir(): 
            try: 
                os.rmdir(dir) 
            except: 
                pass
clean()