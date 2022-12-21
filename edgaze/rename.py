import glob
import os

# For images from NVGaze
# filelist = glob.glob('openEDS/S_0/type_img_frame_*.png')
# filelist = [file.replace("\\", "/") for file in filelist]
# adjusted_filelist = [int(file.replace('openEDS/S_0/type_img_frame_', '').replace(".png", '')) for file in filelist]
# final_filelist = [f"openEDS/S_0/{file}.png" for file in adjusted_filelist]
# for old, new in zip(filelist, final_filelist):
#     os.rename(old, new)
#     print(old, new)

# For images from event-based-gaze-tracking
filelist = glob.glob('openEDS/S_2/*.png')
filelist = [file.replace("\\", "/") for file in filelist]
adjusted_filelist = [file.replace('openEDS/S_2/', '').replace(".png", '') for file in filelist]
final_filelist = [f"openEDS/S_2/{int(file.split('_', 1)[0]) - 1}.png" for file in adjusted_filelist]
for old, new in zip(filelist, final_filelist):
    os.rename(old, new)
    print(old, new)