from os import walk

def split_file(file, prefix, max_size, buffer=1024*1024):
    """
    file: the input file
    prefix: prefix of the output files that will be created
    max_size: maximum size of each created file in bytes
    buffer: buffer size in bytes

    Returns the number of parts created.
    """
    with open(file, 'r+b') as src:
        suffix = 0
        while True:
            if(suffix < 10):
                suffix_str = '0' + str(suffix)
            else:
                suffix_str = str(suffix)
            with open(prefix + '.%s' % suffix_str, 'w+b') as tgt:
                written = 0
                while written < max_size:
                    data = src.read(buffer)
                    if data:
                        tgt.write(data)
                        written += buffer
                    else:
                        return suffix
                suffix += 1

# 分割成一百以内的都可以
def cat_files(files_dir, outfile, buffer=1024):
    """
    infiles: a list of files
    outfile: the file that will be created
    buffer: buffer size in bytes
    """
    f = []
    for (dirpath, dirnames, filenames) in walk(files_dir):
        for filename in filenames:
            f.append(dirpath + "/" + filename)
    with open(outfile, 'w+b') as tgt:
        for infile in sorted(f):
            with open(infile, 'r+b') as src:
                while True:
                    data = src.read(buffer)
                    if data:
                        tgt.write(data)
                    else:
                        break


if __name__ == '__main__':
    open_file = 'C:/Users/zengtao/Desktop/lijiu.vsd'
    prefix = 'C:/Users/zengtao/Desktop/splits_file/lijiu.vsd'
    # split_file(open_file, prefix, 10240)
    cat_files('C:/Users/zengtao/Desktop/splits_file', 'C:/Users/zengtao/Desktop/splits_file/lijiu.vsd')
