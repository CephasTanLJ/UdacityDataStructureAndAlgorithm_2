#%%
import os

def find_files(suffix, path):
    """
        Find all files beneath path with file name suffix.

        Note that a path may contain further subdirectories
        and those subdirectories may also contain further subdirectories.

        There are no limit to the depth of the subdirectories can be.

        Args:
          suffix(str): suffix if the file name to be found
          path(str): path of the file system

        Returns:
           a list of paths
    """
    target_list = list()
    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            target_list.extend(find_files(suffix, filepath))
        elif os.path.isfile(filepath) and filepath.endswith(suffix):
            target_list.append(filepath)
    return target_list



print(find_files('.c', './testdir'))

