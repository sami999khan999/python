# copying a file

# To copy a file in Python, you can use the shutil module, which provides a convenient way to handle high-level file operations such as copying, moving, and removing files.

import shutil

# ===================================================================================================== #

# copyfile()

# To use the copyfile() method from the shutil module to copy a file, follow the example below. This function is a lower-level file copying method that only copies the file's content, without preserving file metadata such as permissions or timestamps.

shutil.copyfile("text.txt", "copyfile.txt")

# ===================================================================================================== #

# copy()

# shutil.copy(src, dst): Copies the file from the source path (src) to the destination path (dst). It copies the content and the file permissions but does not copy metadata like modification times.

shutil.copy("text.txt", "copy.txt")

# ===================================================================================================== #

# copy2()

# shutil.copy2(src, dst): Similar to copy(), but also copies metadata like file creation and modification times.

shutil.copy2("text.txt", "copy2.txt")
