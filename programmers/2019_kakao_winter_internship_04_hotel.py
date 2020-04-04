def solution(k, room_number):
    answer = []
    room_map = {}
    
    for n in room_number:
        keys = room_map.keys()
        if n not in keys: 
            room_map[n] = n+1
        else:
            m = n
            while(n in keys):
                n = room_map[n]
            room_map[m] = n+1
            room_map[n] = n+1
        answer.append(n)
    
    return answer