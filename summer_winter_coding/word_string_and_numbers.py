# https://programmers.co.kr/learn/courses/30/lessons/81301

dic = {
    "zero" : 0,
    "one"  : 1,
    "two"  : 2,
    "three": 3,
    "four" : 4,
    "five" : 5,
    "six"  : 6,
    "seven": 7,
    "eight": 8,
    "nine" : 9,
}
lst = ["zero","one","two","three","four","five","six","seven","eight","nine"]

def solution(s):
    for i in lst:
        s = s.replace(i,str(dic[i])) #s= 으로 지정해줘야함
    return s

print(solution("one4seveneight"))