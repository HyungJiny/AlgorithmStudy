def solution(s):
    answer = []
    n_tuple = [l.split(',') for l in s[1:-2].replace('{', '').split('},')]
    n_tuple.sort(key=lambda x: len(x))
    for n in n_tuple:
        answer += [int(e) for e in n if int(e) not in answer]
    
    return answer