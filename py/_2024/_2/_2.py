from .common import report_safe, parse
from itertools import chain

def enumerate_reports(report):
    for i in range(len(report)):
        yield report[:i] + report[i+1:]

def answer(file):
    safe_reports = 0
    for orig_report in parse(file):
        orig_report = list(orig_report)
        for report in chain([orig_report], enumerate_reports(orig_report)):
            if report_safe(report):
                safe_reports += 1
                break
    return safe_reports

