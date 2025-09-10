import os
from dataclasses import dataclass, field
from typing import Dict, Union

@dataclass
class File:
    name: str
    contents: str

@dataclass
class Folder:
    name: str
    contents: Dict[str, Union["Folder", File]] = field(default_factory=dict)

class VirtualFS:
    def __init__(self, name: str, maxstorage_mb: int = 1024, minstorage_bit: int = 0) -> None:
        self.name = name
        self.max, self.min = maxstorage_mb, minstorage_bit
        self.root = Folder("root")

    def createFile(self, f: File, parent: Folder):
        if parent is None:
            parent = self.root
        parent.contents[f.name] = f

    def createFolder(self, fl: Folder, parent: Folder):
        if parent is None:
            parent = self.root
        parent.contents[fl.name] = fl

    def readFile(self, filename: str, parent: Folder) -> str:
        if not parent:
            parent = self.root
        item = parent.contents.get(filename)
        if isinstance(item, File):
            return item.contents
        raise FileNotFoundError(f"No file named {filename} in {parent.name}")

# Optional: write to real filesyste
def createFile(path: str, contents: str):
    with open(path, "w") as f:
        f.write(contents)

def createFolder(path: str, exist_ok=False):
    os.makedirs(path, exist_ok=exist_ok)
