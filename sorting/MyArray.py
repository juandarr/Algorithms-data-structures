class MyArray():
    '''
    Class MyArray

    Stores an array and allows the application of 
    several sorting methods

    '''
    def __init__(self, arr):
        self.arr = arr

    def __repr__(self):
        return '{}'.format(self.arr)

    def bubble_sort(self):
        range_unsorted = len(self.arr)-1
        step = 0
        unsorted = True

        while unsorted:
            unsorted = False    
            for i in range(range_unsorted):
                step += 1
                print('step {}'.format(step))
                if (self.arr[i]>self.arr[i+1]):
                    tmp = self.arr[i]
                    self.arr[i] = self.arr[i+1]
                    self.arr[i+1] = tmp
                    unsorted=True
                    step += 1
                    print('step {}: swap!'.format(step))
            range_unsorted -= 1
    
    def selection_sort(self):
        starting_index = 0
        step = 0
        while starting_index<len(self.arr)-1:
            min_value_index = starting_index
            for i in range(starting_index+1, len(self.arr)):
                step += 1
                print('step {}'.format(step))
                if (self.arr[i] < self.arr[min_value_index]):
                    min_value_index = i
            if (starting_index!=min_value_index):
                step += 1
                print('step {}. Value swap.'.format(step))
                tmp = self.arr[starting_index]
                self.arr[starting_index] = self.arr[min_value_index]
                self.arr[min_value_index] = tmp
            starting_index += 1

    def insertion_sort(self):
        starting_index = 1
        step = 0
        while starting_index <= len(self.arr)-1:
            temp_val = self.arr[starting_index]
            gap_index = starting_index
            for i in range(starting_index-1,-1,-1):
                step += 1
                print('step {}'.format(step))
                if self.arr[i]>=temp_val:
                    step += 1
                    print('step {}. Insert to right.'.format(step))
                    self.arr[i+1]= self.arr[i]
                    gap_index = i
                if (i==0 or self.arr[i]< temp_val):
                    step += 1
                    print('step {}. Final insert.'.format(step))
                    self.arr[gap_index] = temp_val
                    break
            starting_index += 1
    
    def quicksort(self):

        self.step = 0

        def swap(left_pointer, right_pointer):
            tmp = self.arr[left_pointer]
            self.arr[left_pointer] = self.arr[right_pointer]
            self.arr[right_pointer] = tmp

        def partitioning(left_pointer, right_pointer):
            pivot = self.arr[right_pointer]
            pivot_position = right_pointer
            right_pointer -= 1

            while True:
                while (self.arr[left_pointer] < pivot):
                    left_pointer += 1    

                while (self.arr[right_pointer] >= pivot):
                    right_pointer -= 1

                if (left_pointer >= right_pointer):
                    swap(left_pointer, pivot_position)
                    break
                else:
                    swap(left_pointer, right_pointer)
                    left_pointer += 1
                    right_pointer -= 1
                    
            return left_pointer
        
        def qs(left_pointer, right_pointer):
            if (left_pointer >= right_pointer):
                return
            pivot = partitioning(left_pointer, right_pointer)
            qs(left_pointer, pivot-1)
            qs(pivot+1, right_pointer)

        lp = 0
        rp = len(self.arr)-1
        qs(lp,rp)


                


