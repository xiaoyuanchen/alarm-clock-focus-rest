import sys
import time
import datetime
import pygame


# 实现闹钟功能
def alert():
    music = input("请设置铃声（路径）: ")  # D:\lishao-yyqx.mp3
    study_time = int(input("请设置上课时长（分钟）: "))
    rest_time = int(input("请设置休息时长（分钟）: "))
    start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    while True:
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sys.stdout.write('上课中: '+now + '\r')
        sys.stdout.flush()
        time.sleep(1)

        t1 = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')  # 上课时间
        t2 = datetime.datetime.strptime(now, '%Y-%m-%d %H:%M:%S')  # 下课时间
        
        if (t2 - t1).seconds == (study_time * 60):
            pygame.mixer.init()  # 初始化
            pygame.mixer.music.load(music)  # 加载音乐
            pygame.mixer.music.play()  # 播放音乐
            while 1:
                now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                sys.stdout.write('下课中：'+now + '\r')
                sys.stdout.flush()
                if pygame.mixer.music.get_busy():  # 音乐放
                    if ((datetime.datetime.strptime(now, '%Y-%m-%d %H:%M:%S') - t2).seconds < (rest_time * 60)):  # 时间未到
                        time.sleep(1)
                    else:  # 时间到了
                        pygame.mixer.music.stop()
                        break
                else:  # 音乐停
                    if ((datetime.datetime.strptime(now, '%Y-%m-%d %H:%M:%S') - t2).seconds < (rest_time * 60)):  # 时间未到
                        pygame.mixer.music.play()
                        time.sleep(1)
                    else:  # 时间到了
                        break
            start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def main():
    alert()


if __name__ == "__main__":
    main()
