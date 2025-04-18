from os import walk
import os
import ntpath
import shutil


def split_file(file, max_size, progress_bar, buffer=4 * 1024 * 1024):
    """
    file: the input file
    prefix: prefix of the output files that will be created
    max_size: maximum size of each created file in bytes
    buffer: buffer size in bytes

    Returns the number of parts created.
    """
    split_dir = file + "-split-file/"
    if os.path.isdir(split_dir):
        shutil.rmtree(split_dir)
    os.mkdir(split_dir)
    path, filename = ntpath.split(file)
    prefix = split_dir + filename
    writen_count = 0
    with open(file, 'r+b') as src:
        suffix = 0
        while True:
            if (suffix < 10):
                suffix_str = '0' + str(suffix)
            else:
                suffix_str = str(suffix)
            with open(prefix + '.%s' % suffix_str, 'w+b') as tgt:
                written = 0
                while written < max_size:
                    data = src.read(buffer)
                    if data:
                        writen_count += buffer
                        progress_bar['value'] = writen_count
                        print(writen_count)
                        tgt.write(data)
                        written += buffer
                    else:
                        return suffix
                suffix += 1


# 分割成一百以内的都可以
def cat_files(files_dir, progress_bar, buffer=40 * 1024 * 1024):
    """
    infiles: a list of files
    outfile: the file that will be created
    buffer: buffer size in bytes
    """

    f = []
    for (dirpath, dirnames, filenames) in walk(files_dir):
        for filename in filenames:
            f.append(dirpath + "/" + filename)
    outfile = f[0].split(".00")[0]
    read_count = 0
    with open(outfile, 'w+b') as tgt:
        for infile in sorted(f):
            with open(infile, 'r+b') as src:
                while True:
                    data = src.read(buffer)
                    if data:
                        read_count += buffer
                        print(read_count)
                        progress_bar['value'] = read_count
                        tgt.write(data)
                    else:
                        break


if __name__ == '__main__':
    print("123")
    print("456")
    open_file = 'C:/Users/zengtao/Desktop/lijiu.vsd'
    # prefix = 'C:/Users/zengtao/Desktop/splits_file/lijiu.vsd'
    # split_file(open_file, prefix, 10240)
    # cat_files('C:/Users/zengtao/Desktop/splits_file', 'C:/Users/zengtao/Desktop/splits_file/lijiu.vsd')
