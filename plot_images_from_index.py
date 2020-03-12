import os
import cv2

base_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),'dataset')
test_dir = os.path.join(base_dir, 'test')
b_index = [5, 7, 8, 11, 14, 17, 19, 23, 34, 77, 82, 84, 86, 87, 93, 102]
#####

sub_dirs = [dir for dir in os.listdir(test_dir) if os.path.isdir(os.path.join(test_dir, dir))]
sub_dirs.sort()
i = -1
for path in sub_dirs:
    path = os.path.join(test_dir, path)
    files = os.listdir(path)
    files.sort()
    for file in files:
        i = i + 1
        if i not in b_index:
            continue
        file = os.path.join(path, file)
        if os.path.isfile(file):
            img = cv2.imread(file)
            cv2.imshow('image', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
