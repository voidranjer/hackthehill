import time
import vlc
import asyncio
import websockets
import serial




URI = "ws://172.20.10.2:8765"

ser = serial.Serial('COM4', 9800, timeout=1)
time.sleep(2)


async def listen():
    async with websockets.connect(URI) as websocket:
        while True:
            res = await websocket.recv()
            print(f"> {res}")

            if res == "plastic":
                led1()
            elif res == "metal":
                led2()
            elif res == "carboard":
                led3()
            elif res == "landfill":
                led4()
            elif res == "nothing":
                ledOff()

            await asyncio.sleep(1)


def led1():
    ledOff()
    ser.write(b'1')
    play_file("file:///hack_the_hill_left_en.wav")
    play_file("file:///hack_the_hill_left_fr.wav")
    play_file("file:///hack_the_hill_left_cn.wav")

def led2():
    ledOff()
    ser.write(b'2')
    play_file("file:///hack_the_hill_right_en.wav")
    play_file("file:///hack_the_hill_right_fr.wav")
    play_file("file:///hack_the_hill_right_cn.wav")

def led3():
    ledOff()
    ser.write(b'3')
    play_file("file:///hack_the_hill_middle_en.wav")
    play_file("file:///hack_the_hill_middle_fr.wav")
    play_file("file:///hack_the_hill_middle_cn.wav")

def led4():
    ledOff()
    ser.write(b'3')
    # make sure to add sound files

def ledOff():
    ser.write(b'5')

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
