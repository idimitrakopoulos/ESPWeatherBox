import time

def scroll_down_show(oled, line_to_show):

    for y in range(0, -6, -1):
        time.sleep(0.01)
        oled.scroll(0, y)

        if y == -5:
            oled.text(line_to_show, 0, 15)
        oled.show()
