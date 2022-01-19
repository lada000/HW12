class MyTime:
    def __init__(self, hours=None, minutes=None, seconds=None):
        if type(hours) == type(minutes) == type(seconds) == int:
            self._hours = hours
            self._minutes = minutes
            self._seconds = seconds
        elif type(hours) == str:
            tmp = hours.split(":")
            self._hours = int(tmp[0])
            self._minutes = int(tmp[1])
            self._seconds = int(tmp[2])
        elif isinstance(hours, MyTime):
            self._hours = hours._hours
            self._minutes = hours._minutes
            self._seconds = hours._seconds
        elif hours == minutes == seconds is None:
            self._hours = 0
            self._seconds = 0
            self._minutes = 0
    def get_time(self):
        print(f"{self._hours}:{self._minutes}:{self._seconds}")

    def __eq__(self, other):
        return (self._hours == other._hours) and (self._minutes == other._minutes) and (self._seconds == other._seconds)

    def __ne__(self, other):
        return (self._hours != other._hours) or (self._minutes != other._minutes) or (self._seconds != other._seconds)

    def __ge__(self, other):
        return ((self._hours * 60 + self._minutes) * 60 + self._seconds) >= ((other._hours * 60 + other._minutes) * 60 + other._seconds)

    def __le__(self, other):
        return ((self._hours * 60 + self._minutes) * 60 + self._seconds) <= ((other._hours * 60 + other._minutes) * 60 + other._seconds)

    def __lt__(self, other):
        return ((self._hours * 60 + self._minutes) * 60 + self._seconds) < ((other._hours * 60 + other._minutes) * 60 + other._seconds)

    def __gt__(self, other):
        return ((self._hours * 60 + self._minutes) * 60 + self._seconds) > ((other._hours * 60 + other._minutes) * 60 + other._seconds)

    def __add__(self, other):
        hours = self._hours + other._hours
        minutes = self._minutes + other._minutes
        seconds = self._seconds + other._seconds
        if seconds >= 60:
            seconds -= 60
            minutes += 1
        if minutes >= 60:
            minutes -= 60
            hours += 1
        if hours == 48:
            hours = 0
        elif hours > 48:
            hours -= 48
        elif hours >= 24:
            hours -= 24
        print(f"{hours}:{minutes}:{seconds}")

    def __sub__(self, other):
        hours = self._hours - other._hours
        minutes = self._minutes - other._minutes
        seconds = self._seconds - other._seconds
        if seconds < 0:
            seconds *= -1
            seconds = 60 - seconds
            minutes -= 1
        if minutes <0:
            minutes *= -1
            minutes = 60 - minutes
            hours -= 1
        if hours < 0:
            hours *= -1
        print(f"{hours}:{minutes}:{seconds}")

    def __mul__(self, other):
        hours = self._hours * other
        minutes = self._minutes * other
        seconds = self._seconds * other
        if seconds >= 60:
            t = seconds // 60
            minutes -= t
            seconds = seconds - 60*t
        if minutes >= 60:
            t = minutes // 60
            hours -= t
            minutes = minutes - 60*t

        if hours >= 24:
            t = hours // 24
            hours = hours - t*24
        print(f"{hours}:{minutes}:{seconds}")




time0 = MyTime(9, 10, 2)
time1 = MyTime("8:22:20")
time2 = MyTime(time0)
time1.get_time()
time2.get_time()

print(time1 == time2)
print(time1 != time2)
print(time1 >= time2)
print(time1 <= time2)
print(time1 < time2)
print(time1 > time2)
time1+time2
time1-time2
time1*7