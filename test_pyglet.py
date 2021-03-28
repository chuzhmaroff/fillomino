import cv2
import os

path_to_script = os.path.dirname(os.path.abspath(__file__))
path_to_background = r'{}/background.png'.format(path_to_script)

path_to_video = r'{}/test_video.avi'.format(path_to_script)
out = cv2.VideoWriter(path_to_video, cv2.VideoWriter_fourcc('M','J','P','G'), 0.5, (741, 741)) 
out.write(cv2.imread(path_to_background))
out.write(cv2.imread(path_to_background))
out.write(cv2.imread(path_to_background))
out.write(cv2.imread(path_to_background))
"""out.write(cv2.imread('C://bdseoru2.png'))
out.write(cv2.imread('C://bdseoru3.png'))
out.write(cv2.imread('C://bdseoru4.png'))"""
out.release() #генерируем
cv2.destroyAllWindows() #завершаем