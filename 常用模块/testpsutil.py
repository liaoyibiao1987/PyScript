import psutil


def test1():
    print(psutil.cpu_count())
    print(psutil.cpu_count(logical = False))
    print(psutil.cpu_times())

    #for x in range(3):
    #    psutil.cpu_percent(interval=1)

    #for x in range(3):
    #    psutil.cpu_percent(interval=1, percpu=True)

    #for x in range(3):
    #    psutil.cpu_times_percent(interval=1, percpu=False)
    print(list(psutil.win_service_iter()))
test1()