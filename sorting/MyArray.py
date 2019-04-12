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

                


