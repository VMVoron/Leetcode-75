class Solution(object):
    def moveZeroes(self, nums):
    # Инициализируем указатель для ненулевых элементов
        left = 0
        
        # Проходим по всем элементам массива
        for right in range(len(nums)):
            # Если текущий элемент равен 0, просто продолжаем
            if nums[right] == 0:
                continue
            # Если текущий элемент не равен 0, помещаем его на позицию left
            nums[left] = nums[right]
            left += 1  # Увеличиваем указатель left

        # После того как все ненулевые элементы собраны в начале,
        # заполняем оставшиеся позиции нулями
        for i in range(left, len(nums)):
            nums[i] = 0

        return nums
