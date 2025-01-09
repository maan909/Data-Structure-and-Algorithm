class check:
    def sorted_rotated(array: list):
        count = 0
        length = len(array)
        if length == 1:
            print("given array is sorted and rotated, length is 1")
        else:
            for i in range(length):
                if array[i] > array[(i+1)%length]:
                    count+=1
        
            if count <= 1:
                print("Given Array/List is sorted and rotated")
            else: 
                print("Given array is not sorted and rotated")

if __name__=='__main__':
    num = [4,5,1,6,2,3]
    num2=[2]
    obj = check
    obj.sorted_rotated(num)
