def solution(wallet, bill):
    answer = 0
    while min(bill) > min(wallet) or max(bill) > max(wallet):
        bill.sort()
        bill[1] = bill[1] //2
        answer+=1
        
    bill.sort()
    print(bill)
    
    return answer