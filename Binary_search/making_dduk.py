import sys
# 길이가 일정하지 않은 떡볶이 떡
# 그러나 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰줌
# 절단기에 높이 H 를 지정하면 줄지어진 떡을 한번에 절단.
# 높이가 H보다 긴 떡은 H 위의 부분이 잘리고, 낮은 떡은 잘리지 않는다

# ex) 절단기 높이가 15cm인데, 떡들의 높이가 19,14,10,17이면 자른 뒤 떡의 높이는 
# 15,14,10,15 / 잘린 떡의 길이는 차례대로 4,0,0,2  손님은 6cm 만큼의 길이를 가져감

# 손님이 요청한 총 길이가 m 일때 적어도 m 만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값 구하기

# 떡의 개수 n
n,m = map(int,input().split()) # 1<=n<=1000000 # 1<=m<=2,000,000,000 #순차탐색으로 해결하면 시간제한 2초에 걸림
# 이진탐색 사용시 2의 31승이 21억이므로 대략 30 * 100만 : 3000만 연산횟수

heights = list(map(int,sys.stdin.readline().split()))

start = 0 # 이진탐색의 시작점과 끝점 지정
end = max(heights)

result = 0 
while start<=end: # while 이진탐색 수행
    total = 0 # 잘랐을때 떡의 양
    mid = (start+end) // 2
    for x in heights: 
        if x > mid: # 떡 길이가 mid보다 길다면
            total += x - mid # 잘랐을때 떡 양에 더해줌
    
    if total < m: # 만약 원하는 양보다 잘린 떡이 부족하다면 너무 높게 짤랐단 뜻이므로, 자르는 높이를 낮춰줌(왼쪽 탐색)
        end = mid-1
    else:         # 만약 원하는 양보다 잘린 떡이 충분하다면 너무 낮게 짤랐단 뜻이므로, 자르는 높이를 높여줌(오른쪽 탐색)
        result = mid # 자르는 높이를 높여주다가..탐색 범위가 역전되면 이때의 중간값이 리턴됨(최대한 덜 자르는게 목적)
        start  = mid + 1
    
print(result)
    
        
