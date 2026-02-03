def solution(wallet, bill):
    answer = 0
    while min(bill) > min(wallet) or max(bill) > max(wallet):
        bill.sort()
        bill[1] = bill[1] //2
        answer+=1
        
    bill.sort()
    print(bill)
    
    return answer

#--------------------------------
다른사람풀이
#---------------------------------
def solution(wallet, bill):

    wallet, bill = sorted(wallet), sorted(bill)
    cnt = 0
    while wallet[0] < bill[0] or wallet[1] < bill[1]:
        bill[-1] //= 2
        bill = sorted(bill)
        cnt += 1

    return cnt
