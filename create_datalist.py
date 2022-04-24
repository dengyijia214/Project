import os
import numpy as np


def make_datalist(data_fd, data_list):
    filename_all = os.listdir(data_fd)
    filename_all = [data_fd+'/'+filename+'\n' for filename in filename_all if filename.endswith('.tfrecords')]

    np.random.shuffle(filename_all)
    np.random.shuffle(filename_all)
    with open(data_list, 'w') as fp:
        fp.writelines(filename_all)


if __name__ == '__main__':
    data_fd = './data/train&val/mr_train_tfs'
    data_list = './data/datalist/mr_train_tfs.txt'

    make_datalist(data_fd, data_list)
    
if __name__ == '__main__':
    data_fd = './data/train&val/ct_train_tfs'
    data_list = './data/datalist/ct_train_tfs.txt'

    make_datalist(data_fd, data_list)
    
if __name__ == '__main__':
    data_fd = './data/train&val/mr_val_tfs'
    data_list = './data/datalist/mr_val_tfs.txt'

    make_datalist(data_fd, data_list)
    
if __name__ == '__main__':
    data_fd = './data/train&val/ct_val_tfs'
    data_list = './data/datalist/ct_val_tfs.txt'

    make_datalist(data_fd, data_list)
