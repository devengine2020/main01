import pyautogui
from time import sleep, strftime
import math


def move_mouse_gohey():
    r = 60
    (mx, my) = pyautogui.size()
    pyautogui.moveTo(round(mx / 2), round(my / 2 - r - r))
    rad2deg = 360 / math.pi
    move_num = 40
    for t in range(move_num):
        round_t = 3
        step = 1 / (move_num / round_t)
        x = r * math.cos(step * t * 2 * math.pi)
        y = r * math.sin(step * t * 2 * math.pi)
        pyautogui.move(x, y)
    pyautogui.press('shift')


def initialize():
    val = 0
    print("Enterで動作開始 / 1入力+Enterで待機時間設定")
    val = input()
    if val == "1":
        print("Setting:何分間マウス操作がない場合に、ゆらゆらしますか？[1〜30で指定可能です]")
        val = input()
        if val.isdecimal() and int(val) > 1 and int(val) < 31:
            print("動作を開始します。", val, "分間マウス操作がない場合は、ゆらゆらします。")
        else:
            val = 3
            print("動作を開始します。", val, "分間マウス操作がない場合は、ゆらゆらします。")
    else:
        val = 3
        print("動作を開始します。", val, "分間マウス操作がない場合は、ゆらゆらします。")
    return int(val)


def move_mouse_top():
    wait_min = initialize()
    count_sleep = 0
    print(format(strftime('%H:%M:%S')), "Count:", count_sleep, "Min")
    pos_orig = pyautogui.position()

    wait_min = int(wait_min)

    # 推奨
    # max_min = 60*8 # 8 hours
    # check_min = 60 #[sec]

    # 動作確認用
    max_min = 10  # 10 [min]
    check_min = 5  # [sec]

    for idx in range(max_min):
        sleep(check_min)
        pos_current = pyautogui.position()
        dx = pos_orig.x - pos_current.x
        dy = pos_orig.y - pos_current.y
        dist = pow(dx * dx + dy * dy, 0.5)
        pos_orig = pos_current
        if dist < 20:
            count_sleep += 1
        else:
            count_sleep = 0

        print(format(strftime('%H:%M:%S')), "Count:", count_sleep, "Min")

        if count_sleep > wait_min - 1:
            print("moved")
            move_mouse_gohey()
            count_sleep = 0
            print(format(strftime('%H:%M:%S')), "Count", count_sleep, "Min")


# Main
move_mouse_top()
