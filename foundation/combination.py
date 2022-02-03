def combination(arr, r):
    global chosen, used

    # 선택리스트에 조의 원소를 저장하다가 갯수가 r개가 되면 출력 후 함수를 종료한다.
    if len(chosen) == r:
        print(chosen)
        return

    # chosen(뽑은 조합 원소)가 없으면 start = 0으로
    # 그 외에는 뽑은 조합의 가장 마지막 요소를 값의 인덱스 출력
    start = arr.index(chosen[-1]) + 1 if chosen else 0
    for nxt in range(start, len(arr)):
        # 만약 아직 뽑지 않았고, ~~ 조건이라면
        if used[nxt] == 0 and (nxt == 0 or arr[nxt-1] != arr[nxt] or used[nxt-1]):
            # 다음 요소를 뽑고 방문처리한다.
            chosen.append(arr[nxt])
            used[nxt] = 1
            # 다 뽑았으면 마지막 요소부터 pop하고 방문해제한다.
            combination(arr, r)
            chosen.pop()
            used[nxt] = 0


arr = [1, 2, 3, 4, 5, 6 , 7]
chosen = []
used = [0 for _ in range(len(arr))]

combination(arr, 3)