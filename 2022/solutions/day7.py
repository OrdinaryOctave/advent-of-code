#input loaded and ready to go at 05:00:46

class Directory:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.children = []
        self.size = 0
        self.parent = parent

def directorySize(rootDir):
    size = rootDir.size
    for dir in rootDir.children:
        size += directorySize(dir)
    return size

def smallDirectorySize(rootDir):
    sum = 0
    size = directorySize(rootDir)
    if size <= 100000:
        sum += size
    for dir in rootDir.children:
        sum += smallDirectorySize(dir)
    return sum

def getDirectorySizes(rootDir, sizes):
    sizes.append(directorySize(rootDir))
    for dir in rootDir.children:
        sizes = getDirectorySizes(dir, sizes)
    return sizes

with open('2022/inputs/day7') as f:
    root = Directory("/", None)
    currentDirectory = root
    instruction = f.readline()
    
    while instruction != "":
        if instruction.__contains__("cd"):
            targetDirectory = instruction.split(" ")[2]
            
            if targetDirectory == "..":
                currentDirectory = currentDirectory.parent
            else:
                for dir in currentDirectory.children:
                    if dir.name == targetDirectory:
                        currentDirectory = dir
                        break
            instruction = f.readline().rstrip("\n")
            
        elif instruction.__contains__("ls"):
            line = f.readline().rstrip("\n")
            file = line.split(" ")
            
            while (file[0] != "$" and file[0] != ""):
                if file[0] == "dir":
                    currentDirectory.children.append(Directory(file[1], currentDirectory))
                else:
                    currentDirectory.size += int(file[0])
                
                line = f.readline().rstrip("\n")
                file = line.split(" ")
                
            instruction = line
        
        else:
            print(f"problem on line {instruction}")
            instruction = f.readline().rstrip("\n")
        
print(smallDirectorySize(root))

usedSpace = directorySize(root)
availableSpace = 70000000-usedSpace
sizeToDelete = 30000000-availableSpace
directorySizes = getDirectorySizes(root, [])
directorySizes.sort(reverse=True)

dirToDelete = 0
for dir in directorySizes:
    if dir > sizeToDelete:
        dirToDelete = dir
    else:
        break

print(dirToDelete)