import sys, signal
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

from threading import Timer
from time import sleep


class Timer(Timer):
    """
    See: https://hg.python.org/cpython/file/2.7/Lib/threading.py#l1079
    """

    def run(self):
        while not self.finished.is_set():
            self.finished.wait(self.interval)
            self.function(*self.args, **self.kwargs)

        self.finished.set()


def take_20s_break():
    Notify.init("break")
    break20 = Notify.Notification.new("20-20-20 rule: Look away!",
                                    "It's time to look at something 20 feet "
                                    "away for 20 s",
                                    "dialog-information")
    break20.show()

def back_at_it():
    Notify.init("back")
    back20 = Notify.Notification.new("20-20-20 rule: Go back to work!",
                                    "You can go back to work for another 20 "
                                    "minutes.",
                                    "dialog-information")
    back20.show()

def main(args=None):
    """The main routine."""
    # if args is None:
    #     args = sys.argv[1:]
    #
    # print("This is the main routine.")
    # print("It should do something interesting.")
    # # Do argument parsing here (eg. with argparse) and anything else
    # # you want your project to do.


    r1 = Timer(20*60-20., take_20s_break)
    r2 = Timer(20*60, back_at_it)
    try:
        r1.start()
        r1.join()
        r2.start()
        r2.join()
    except KeyboardInterrupt:
        r2.cancel()
        r1.cancel()
        sys.exit(0)


if __name__ == "__main__":
    main()
