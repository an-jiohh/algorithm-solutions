def solution(words):
    root = {"ch":{}, "count":0, "end":False}
    
    for word in words:
        node = root
        node["count"] += 1
        for w in word :
            node["ch"][w] = node["ch"].get(w, {"ch":{}, "count":0, "end":False})
            node = node["ch"][w]
            node["count"] += 1
        node["end"] = True
    answer = 0
    for word in words:
        node = root
        typed = 0
        for w in word:
            node = node["ch"][w]
            typed += 1
            if node["count"] == 1 :
                break
        answer += typed

    return answer