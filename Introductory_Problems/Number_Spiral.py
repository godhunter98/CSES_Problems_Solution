# firstly lets collect the total number of tests were gonna do
number_of_tests = int(input())


# Then add all the cases we're gonna try in a list, this is a just a long list with each X,Y in an array
ls = []
for i in range(number_of_tests):
    nums = input().split(' ')
    ls.extend(nums)

#This is where we loop over each pair of X,Y and get their corresponding values
for i in range(0,len(ls),2):
    y = int(ls[i])
    x = int(ls[i+1])
 
    def spiral_position(x=x,y=y):
        if y>x:
            if y%2==0:
                output = y**2-(x-1)
            else:
                output = (y-1)**2+x
        else:
            if x%2==0:
                output = (x-1)**2 + y
            else:
                output = x*x-(y-1)
        return output
    print(spiral_position())
