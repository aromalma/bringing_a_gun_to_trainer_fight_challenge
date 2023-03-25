def solution(dimensions, your_position, trainer_position, distance):
    import math
    # function to get all reflections at x,y axis seperately
    def get_ref(dim,point,t,distance):
        temp,v=[-point,point+2*(dim-point)],[point]

        while temp:
            a=temp.pop(0)

            if abs(a-t)>distance:
                continue
            v.append(a)
            if a>0:
                temp.append(-a)
            else:
                temp.append(a+2*(dim-a))
        return v
    
    def polar(a,b):
        x,y=a[0]-b[0],a[1]-b[1]
        return x**2+y**2,math.atan2(x,y) 
    
    distance_sq=distance**2
    sec_ang=set()
    mag,ang=polar(your_position,trainer_position)
    if mag>distance_sq:
        return 0

    fir_mag={ang:mag}
    # axis wise reflections of trainer or enemy (E)
    xt,yt=get_ref(dimensions[0],trainer_position[0],your_position[0],distance),get_ref(dimensions[1],trainer_position[1],your_position[1],distance)
    # axis wise reflections of You (U)
    xu,yu=get_ref(dimensions[0],your_position[0],your_position[0],distance),get_ref(dimensions[1],your_position[1],your_position[1],distance)
    # find all angles and distance of reflections of you
    for x in xu:
        for y in yu:
            mag,ang=polar(your_position,(x,y))
            if mag>distance_sq:
                continue

            if ang not in fir_mag:
                fir_mag[ang]=mag
            else:
                fir_mag[ang]=min(mag,fir_mag[ang])
    
    count=0
    hist=set()
    # find all angles and distance of reflections of enemy
    for x in xt:
        for y in yt:
            
            mag,ang=polar(your_position,(x,y))

            if mag>distance_sq:
                continue
            # check whether that direction already examined
            if ang in hist:
                continue
            
            # check whther you reflections are not coming in between these shots  
            if ang in fir_mag and fir_mag[ang]<mag:
                
                continue

            hist.add(ang)
            count+=1
            
    return count
if __name__ == "__main__":
    solution([3,2], [2,1],[1,1], 4)
