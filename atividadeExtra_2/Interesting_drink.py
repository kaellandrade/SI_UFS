#!python3.8
from math import floor
LEFT = 0


def binary(arr, key, left, right) -> int:
    while(left < right):
        mid = (left+right)//2
        if(arr[mid] <= key):
            left = mid + 1
        else:
            right = mid
    return left


def Interesting_drink():
    number_store = int(input())
    list_store = list(map(int, input().split()))
    list_store.sort()

    price_drink_day = int(input())
    for _ in range(price_drink_day):
        coin = int(input()) 
        print(binary(list_store, coin, 0, len(list_store)))


Interesting_drink()
