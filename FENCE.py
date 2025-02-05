number_of_friends,fence_height=tuple(map(float,input().split()))
height_of_friends=list(map(float,input().split()))
weidth_of_road=0
for height in height_of_friends:
    if height>fence_height:
        weidth_of_road+=2
    else:
        weidth_of_road+=1
print(weidth_of_road)