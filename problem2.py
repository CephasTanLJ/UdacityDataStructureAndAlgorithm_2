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


def test():
    '''Test that all files in the lists contains .c extension.'''
    targetfile_list = find_files('.c', './testdir')
    for file in targetfile_list:
        assert os.path.isfile(file) is True, f"{file} is not a file."
        _, ext = os.path.splitext(file)
        assert ext == '.c', f'File extension of {file} is not ".c".'
    print('test done.')

def test2():
    '''Test for file extensions that do not exits (edge case). An empty list should be returned.'''
    targetfile_list = find_files('.ExtDoesNotExists', './testdir')
    assert len(targetfile_list) == 0, f'test2: Should return an empty list because not files should exists, but {targetfile_list} was returned'
    print('test2 done.')

def test3():
    '''Test for file path that do not exits (edge case). An empty list should be returned.'''
    try:
        targetfile_list = find_files('.c', './dirDoesNotExists')
        assert 'targetfile_list' not in locals(), f'test3: FileNotFoundError should be raised because input path does not exists, but {targetfile_list} was returned.'
    except FileNotFoundError:
        print('FileNotFoundError correctly raised; test3 done.')

if __name__ == '__main__':
    test()
    test2()
    test3()
    print('All pass')