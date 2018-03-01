from bd_app import *
from time import sleep
from queue import Queue
from sw_controller.scan_task import ScanTask

DAYS_FROM_LAST_SCAN = 7
clientdb = Client_DB()
reportdb = Report_DB()

def get_hosts_to_scan(days):
    return ['127.0.0.1']

if __name__ == '__main__':
    while True:
        # Получить список хостов для сканирования
        hosts = get_hosts_to_scan(DAYS_FROM_LAST_SCAN)
        # Для каждого хоста провести скан
        out_queue = Queue()
        for host in hosts:
            scan = ScanTask(host, out_queue)
            scan.start()
            scan.join()

        # Результат скана сохранить в базу
        # Разослать результаты по почте
        # Заснуть, если возможно

