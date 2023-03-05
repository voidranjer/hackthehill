import serial
import time
import vlc
import asyncio
import websockets


URI = "ws://172.20.10.2:8765"

ser = serial.Serial('COM4', 9800, timeout=1)
time.sleep(2)


async def listen():
    async with websockets.connect(URI) as websocket:
        while True:
            res = await websocket.recv()
            print(f"> {res}")

            if res == "gatorade":
                led1()
            elif res == "popcorners":
                led2()
            elif res == "gingerale":
                led3()

            await asyncio.sleep(1)


def led1():
    ser.write(b'1')
    play_file("file:///hack_the_hill_left_en.wav")
    play_file("file:///hack_the_hill_left_fr.wav")
    play_file("file:///hack_the_hill_left_cn.wav")

def led2():
    ser.write(b'2')
    play_file("file:///hack_the_hill_right_en.wav")
    play_file("file:///hack_the_hill_right_fr.wav")
    play_file("file:///hack_the_hill_right_cn.wav")

def led3():
    ser.write(b'3')
    play_file("file:///hack_the_hill_middle_en.wav")
    play_file("file:///hack_the_hill_middle_fr.wav")
    play_file("file:///hack_the_hill_middle_cn.wav")

# function to play a file
def play_file(file):
    p = vlc.MediaPlayer(file)
    p.play()
    print("Playing")
    time.sleep(1)
    while p.is_playing():
        time.sleep(1)
    p.stop()
    print("Done")


# for i in range(2):
#     led1()
#     time.sleep(4)
#     led2()
#     time.sleep(4)
#     led3()
#     time.sleep(4)


if __name__ == "__main__":
    asyncio.run(listen())
