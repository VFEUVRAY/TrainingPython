from time import sleep
import datetime

def ft_progress(prog : list) -> None :
    start = datetime.datetime.now().timestamp()
    my_generator = range(len(prog))
    progress_step = str("=")
    for iter in my_generator:
        current_time = datetime.datetime.now().timestamp()
        time_elapsed = (current_time - start)
        eta_ms_left = (time_elapsed) * (len(prog) - iter)
        purcent = (iter / len(prog)) * 100
        progress_bar = ''.join(['{0}']*(int(purcent/4) + 1)).format(progress_step) + '>'
        print ("ETA: {:.4f}s   ".format(eta_ms_left / 1000), end='')
        print ("{:4}".format("{:.0f}%".format(purcent)), end='')
        print("[{:25.25}]".format(progress_bar), end='') #% tuple(["=" for i in range(progress_bar)]))
        print("%.4f" % (time_elapsed / 1000) + "s elapsed")
        yield iter

listy = range(1000)
ret = 0
for i in ft_progress(listy):
    ret = i * 3
    sleep(0.001)
print(datetime.datetime.now().microsecond)
print(datetime.datetime.now().microsecond)
print(datetime.datetime.now().timestamp())
