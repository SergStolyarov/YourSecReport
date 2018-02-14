from adapters.api import ToolAdapter
from libnmap.process import NmapProcess
from libnmap.parser import NmapParser, NmapParserException


class NmapAdapter(ToolAdapter):
    def __init__(self, ip):
        if self.is_valid_ip(ip):
            self.ip = ip
        else:
            raise ValueError
        self.nmproc = NmapProcess(self.ip, "-sV")
        self.parsed = None

    def start(self):
        rc = self.nmproc.run()
        if rc != 0:
            print("nmap scan failed: {0}".format(self.nmproc.stderr))
        print(type(self.nmproc.stdout))

        try:
            self.parsed = NmapParser.parse(self.nmproc.stdout)
        except NmapParserException as e:
            print("Exception raised while parsing scan: {0}".format(e.msg))


if __name__ == '__main__':
    adapter = NmapAdapter('127.0.0.1')
    adapter.start()
