# https://zulko.github.io/moviepy/getting_started/quick_presentation.html
from moviepy.editor import VideoFileClip

clip1 = VideoFileClip("./test.mp4").subclip(20, 79)
duration = clip1.duration
clip2 = clip1.fl_time(
    lambda t: 1.5 * t, apply_to=["mask", "video", "audio"]
).set_end(duration / 1.5)
clip1.write_videofile("result.mp4")
clip2.write_videofile("result_acc.mp4")
