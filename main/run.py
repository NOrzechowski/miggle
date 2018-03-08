import time
from ctypes import windll, pointer, c_long, c_ulong, Structure


class _point_t(Structure):
    _fields_ = [
        ('x', c_long),
        ('y', c_long),
    ]

def get_cursor_position():
    point = _point_t()
    result = windll.user32.GetCursorPos(pointer(point))
    if result:
        return (point.x, point.y)
    else:
        return None


def set_cursor_position(x, y):
    result = windll.user32.SetCursorPos(c_long(int(x)), c_long(int(y)))
    if result:
        return False
    else:
        return True

while True:
    time.sleep(60 * 5)  # 5 minutes
    x, y = get_cursor_position()
    set_cursor_position(x + 2, y + 2)
    set_cursor_position(x - 2, y - 2)