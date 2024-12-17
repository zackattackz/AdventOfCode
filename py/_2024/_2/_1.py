from .common import report_safe, parse

def answer(file):
    safe_reports = 0
    for report in parse(file):
        if report_safe(list(report)):
            safe_reports += 1
    return safe_reports

