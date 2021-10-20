def BubbleSort(my_list):
    for i in range(len(my_list-1), 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list

class merge_sort:
    def merge(self, list1, list2):
        combined = []
        i = 0
        j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                combined.append(list1[i])
                i += 1
            else:
                combined.append(list2[j])
                j += 1
        while i < len(list1):
            combined.append(list1[i])
            i += 1
        while j < len(list2):
            combined.append(list2[j])
            j += 1
        return combined

    def merge_sort_list(self, my_list):
        if len(my_list) == 1:
            return my_list
        mid = int(len(my_list)/2)
        left = my_list[:mid]
        right = my_list[mid:]
        return self.merge(self.merge_sort_list(left), self.merge_sort_list(right))

class quick_sort:
    def swap(self, my_list, index1, index2):
        temp = my_list[index1]
        my_list[index1] = my_list[index2]
        my_list[index2] = temp

    def pivot(self, my_list, pivot_index, end_index):
        swap_index = pivot_index
        for i in range(pivot_index+1, end_index+1):
            if my_list[i] < my_list[pivot_index]:
                swap_index += 1
                self.swap(my_list, swap_index, i)
        self.swap(my_list, pivot_index, swap_index)
        return swap_index

    def quick_sort_list_helper(self, my_list, left, right):
        if left < right:
            pivot_index = self.pivot(my_list, left, right)
            self.quick_sort_list_helper(my_list, left, pivot_index-1)
            self.quick_sort_list_helper(my_list, pivot_index+1, right)
        return my_list

    def quick_sort_list(self, my_list):
        return self.quick_sort_list_helper(my_list, 0, len(my_list)-1)
