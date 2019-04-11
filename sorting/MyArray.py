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
        pass

