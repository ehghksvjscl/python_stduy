import datetime


class Logger(object):
    def log(self, msg):
        print(msg)


class TimestampLogger(Logger):
    def log(self, msg):
        message = "{ts} {msg}".format(
            ts=datetime.datetime.now(),
            msg=msg,
        )
        super().log(message)


class DateLogger(Logger):
    def log(self, msg):
        message = "{ts} {msg}".format(
            ts=datetime.datetime.now().strftime("%Y-%m-%d"),
            msg=msg,
        )
        super().log(message)


l = Logger()
t = TimestampLogger()
d = DateLogger()

print("Ex3 > ", l.log("Called logger"))
print("Ex3 > ", t.log("Called TimestampLogger"))
print("Ex3 > ", d.log("Called DateLogger"))
