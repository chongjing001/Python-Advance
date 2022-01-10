#### Python3使用ffmpeg、opencv操作音视频文件记录

#####  *opencv*

- ```
  pip install opencv-python
  ```

###### 获取首帧
```python
import cv2

def keyframe_test():
    vidcap = cv2.VideoCapture(r'F:\tools\ffmpeg\bin\time.mp4')
    success, image = vidcap.read()
    if success:
        cv2.imwrite("frame1.jpg", image)  # save frame as JPEG file
        cv2.imshow('frame', image)
        cv2.waitKey()


```



###### 格式信息

```python
def get_source_info_opencv(source_name):
    return_value = 0
    try:
        cap = cv2.VideoCapture(source_name)
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH )
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        fps = cap.get(cv2.CAP_PROP_FPS)
        num_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        print("width:{} \nheight:{} \nfps:{} \nnum_frames:{}".format(width, height, fps, num_frames))
    except (OSError, TypeError, ValueError, KeyError, SyntaxError) as e:
        print("init_source:{} error. {}\n".format(source_name, str(e)))
        return_value = -1
    return return_value
```

###### 参数项

```
capture.get(0)   视频文件的当前位置（播放）以毫秒为单位
capture.get(1)   基于以0开始的被捕获或解码的帧索引
capture.get(2)   视频文件的相对位置（播放）：0=电影开始，1=影片的结尾。
capture.get(3)   在视频流的帧的宽度
capture.get(4)   在视频流的帧的高度
capture.get(5)   帧速率
capture.get(6)   编解码的4字-字符代码
capture.get(7)   视频文件中的帧数
capture.get(8)   返回对象的格式
capture.get(9)   返回后端特定的值，该值指示当前捕获模式
capture.get(10)   图像的亮度(仅适用于照相机)
capture.get(11)   图像的对比度(仅适用于照相机)
capture.get(12)   图像的饱和度(仅适用于照相机)
capture.get(13)   色调图像(仅适用于照相机)
capture.get(14)   图像增益(仅适用于照相机)（Gain在摄影中表示白平衡提升）
capture.get(15)   曝光(仅适用于照相机)
capture.get(16)   指示是否应将图像转换为RGB布尔标志
capture.get(17)   × 暂时不支持
capture.get(18)   立体摄像机的矫正标注（目前只有DC1394 v.2.x后端支持这个功能）
```



##### *ffmpeg*

主机需安装`ffmpeg`

> 方式一
>
> pip install ffmpeg-python; ffmpeg
>
> Ubuntu机器上测试的时候获取不到数据

```python
import ffmpeg

def get_source_info_ffmpeg(source_name):
    return_value = 0
    try:
        info = ffmpeg.probe(source_name, capture_stdout=True, capture_stderr=True)
        # print(info)
        # print("---------------------------------")
        vs = next(c for c in info['streams'] if c['codec_type'] == 'video')
        format_name = info['format']['format_name']
        codec_name = vs['codec_name']
        duration_ts = float(vs['duration_ts'])
        fps = vs['r_frame_rate']
        width = vs['width']
        height = vs['height']
        print("format_name:{} \ncodec_name:{} \nduration_ts:{} \nwidth:{} \nheight:{} \nfps:{}".format(format_name, codec_name, duration_ts, width, height, fps))
    except (OSError, TypeError, ValueError, KeyError, SyntaxError, Exception) as e:
        print("init_source:{} error. {}\n".format(source_name, str(e)))
        return_value = 0
    return return_value
```

>方式二 使用进程调用
>
>此方式成功获取到数据

```python
import subprocess

def use_system_ffmpeg(source_name):

    ffmpeger = subprocess.Popen(
        f'ffprobe -show_streams {source_name}',
        shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr = subprocess.PIPE, encoding='utf-8')
    relog = ffmpeger.stdout.read()
    print('======',relog)
    info_list = relog.split('\n')
    frame_nums = 0
    frame_rate = 0
    for item in info_list:
        if item.startswith('r_frame_rate'):
            frame_rate = int(eval(item.split('=')[1]))
        if item.startswith('nb_frames'):
            frame_nums = int(item.split('=')[1])
            break
    print(frame_nums, frame_rate)
    return frame_nums,frame_rate
```

