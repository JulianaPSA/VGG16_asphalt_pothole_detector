import shutil, os

base_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),'dataset')
test_dir = os.path.join(base_dir, 'test')

sub_dirs = [dir for dir in os.listdir(test_dir) if os.path.isdir(os.path.join(test_dir, dir))]
print(sub_dirs)
# images = []
#
# [print(f_name) for f_name in os.listdir(os.path.join(test_dir, sub_dirs[0])).sort() if os.path.isfile(os.path.join(test_dir, sub_dirs[0], f_name)) ]
#
#
# b_index = [2,5,7,8,11,14,17,19,23,34,77,82,84,86,87,93,102]