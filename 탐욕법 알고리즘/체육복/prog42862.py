def solution(n, lost, reserve):
    reserve_new = set(reserve) - set(lost)
    lost_new = set(lost) - set(reserve)

    for i in reserve_new:
        if i - 1 in lost_new:
            lost_new.remove(i - 1)
        elif i + 1 in lost_new:
            lost_new.remove(i + 1)

    answer = n - len(lost_new)
    return answer