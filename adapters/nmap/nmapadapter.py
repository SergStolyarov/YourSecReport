from adapters.api import ToolAdapter
from libnmap.process import NmapProcess
from libnmap.parser import NmapParser, NmapParserException


class NmapAdapter(ToolAdapter):
    def __init__(self, ip, commandline):
        if self.is_valid_ip(ip):
            self.ip = ip
        else:
            raise ValueError

        if commandline:
            self.commandline = commandline
        else:
            self.commandline = '-sV'
        self.nmproc = NmapProcess(self.ip, self.commandline)

    def start(self):
        rc = self.nmproc.run()  #or .run_background()
        if rc != 0:
            print("nmap scan failed: {0}".format(self.nmproc.stderr))
        print(type(self.nmproc.stdout))

    def status(self):
        if self.nmproc.is_running():
            return 'running: {0}%'.format(self.nmproc.progress)
        else:
            if self.nmproc.has_failed():
                return 'failed'
            elif self.nmproc.is_successful():
                return 'finished (successfully)'
            else:
                return 'stopped'

    def stop(self):
        if self.nmproc.is_running():
            self.nmproc.stop()

    def get_result_json(self):
        report = None
        try:
            report = NmapParser.parse(self.nmproc.stdout)
        except NmapParserException as e:
            print("Exception raised while parsing scan: {0}".format(e.msg))
        starttime = report.started
        endtime = report.endtime
        host = report.hosts[0]
        hoststatus = host.status
        services = []
        for serv in host.services:
            service = {}
            service['port'] = serv.port
            service['protocol'] = serv.protocol
            service['state'] = serv.state
            service['service'] = serv.service
            if len(serv.banner):
                service['banner'] = serv.banner
            services.append(service)


if __name__ == '__main__':
    adapter = NmapAdapter('127.0.0.1')
    adapter.start()
