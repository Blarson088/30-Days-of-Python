from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import * # ImageClip
from PIL import Image

W = 1920
H = 1080
St = 0
En = 10

# grab video files location
#source_path_1 = os.path.join(SAMPLE_INPUTS, 'sample.mp4')
#source_path_2 = os.path.join(SAMPLE_INPUTS, 'TheGoodPlasticTable.mp4')
#grabbing video clips

vidFolder = os.path.join(SAMPLE_INPUTS, 'VideoHolder')

this_dir = os.listdir(vidFolder)
filepaths = [os.path.join(vidFolder, fname) for fname in this_dir if fname.endswith("mp4")]
print(filepaths)

num = 0
lis = []
for i in filepaths:
    #print(i)
    clip = VideoFileClip(i,target_resolution=(H,W))#.subclip(St,En)
    num += int(clip.duration)
    print(int(clip.duration))
    lis.append(clip)

print(num)
print((num/2))
print(lis)
#name dir to be stored
Final_Vid_Dir = os.path.join(SAMPLE_OUTPUTS, "FinalVidDir")

#name video to be outputted
output_video = os.path.join(Final_Vid_Dir, 'FinalVid.mp4')

#creating folder
os.makedirs(Final_Vid_Dir, exist_ok=True)


#final_clip = concatenate_videoclips(lis, method="compose") #compose makes clip frames same size
#final_clip.write_videofile(output_video,fps=30)#"my_concatenation.mp4")

