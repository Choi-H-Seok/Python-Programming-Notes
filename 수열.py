N, M = list(map(int, input().split()))

result = []

def function(result):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    for i in range(1,N+1):
        if i not in result:
            result.append(i)
            function(result)
            result.pop()
    return

function(result)