from .common_data import *


def nmap_rep_generate(report):
    table_header = ["port", "protocol", "state", "service", "banner"]

    head_rep = get_head_doc()

    banner = "Nmap ( http://nmap.org ) scan report for ip {}".format(report.get("host", "None"))
    banner = wraper_html_tag("<h2>", banner, sep="")

    table = get_table(table_header, report["services"])

    body = "\n".join([banner, table])
    body = wraper_html_tag("<body>", body)

    report = "\n".join([head_rep, body])
    report = wraper_html_tag("<html>", report)

    return DOCTYPE + report
