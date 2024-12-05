import heapq
from .parse import parse

def answer(file):
    left_list, right_list = [], []
    for l, r in parse(file):
        heapq.heappush(left_list, l)
        heapq.heappush(right_list, r)
    left_list = heapq.nsmallest(len(left_list), left_list)
    right_list = heapq.nsmallest(len(right_list), right_list)
    differences = []
    for l, r in zip(left_list, right_list):
        differences.append(abs(l - r))
    return sum(differences)

