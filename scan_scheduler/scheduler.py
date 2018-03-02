from bd_app import check_report_time, Client_DB, Report_DB
from time import sleep
from queue import Queue
from sw_controller.scan_task import ScanTask

DAYS_FROM_LAST_SCAN = 7
clientdb = Client_DB()
reportdb = Report_DB()

def get_hosts_to_scan(days):
    if __debug__:  # run with -O
        print('----DEBUG: LOCALHOST IS USED----')
        return [('debug', '127.0.0.1')]
    logins_and_hosts_dict = check_report_time(days)
    hosts = []
    for key, value in logins_and_hosts_dict.items():  # convert {'login', ['ip', 'ip2']} to (login, ip) tuple
        hosts.extend(zip([key] * len(value), value))  # and add to list, to avoid emb. loop later
    return hosts

if __name__ == '__main__':
    while True:
        # Получить список хостов для сканирования
        hosts = get_hosts_to_scan(DAYS_FROM_LAST_SCAN)
        # Для каждого хоста провести скан
        out_queue = Queue()
        for host in hosts:
            print('Scanning {0} for user {1} started'.format(host[1], host[0]))
            scan = ScanTask(host[1], out_queue)
            scan.start()
            scan.join() # т.к. пока 1 сервер, пусть сканятся по очереди
            print('Scanning {0} for user {1} finished'.format(host[1], host[0]))
            for scan in iter(out_queue.get, None):
                # Результат скана сохранить в базу
                reportdb.add_report(login=host[0], target=host[1], report_type=scan[0], report=scan[1])
                print(host[1], scan[0], scan[1])
                out_queue.task_done()
        # Разослать результаты по почте
        # Заснуть, если возможно
        sleep(5*60)
