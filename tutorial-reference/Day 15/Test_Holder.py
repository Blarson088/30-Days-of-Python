
    clip1 = VideoFileClip(source_path_1,target_resolution=(H,W)).subclip(St,En)
    clip2 = VideoFileClip(source_path_2,target_resolution=(H,W)).subclip(St,En)
    print(clip1.size)
    print(clip2.size)

#name dir to be stored
Final_Vid_Dir = os.path.join(SAMPLE_OUTPUTS, "FinalVidDir")

#name video to be outputted
output_video = os.path.join(Final_Vid_Dir, 'FinalVid.mp4')

#creating folder
os.makedirs(Final_Vid_Dir, exist_ok=True)


final_clip = concatenate_videoclips([clip1, clip2], method="compose") #compose makes clip frames same size
final_clip.write_videofile(output_video,fps=30)#"my_concatenation.mp4")




