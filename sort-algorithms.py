import unittest

class Sort:
    """
    Utility class which contains sorting algorithms.
    """
    def bubble(data):
        """
        Iterates through the array until no more values are swapped places.
        Elements are swapped if the current element > next element
        """
        swapped = True
        # terminate subroutine once no more values are swapped
        while swapped:
            swapped = False
            # iterate all values in array
            for index, value in enumerate(data):
                # check if the value is greater than next element
                if len(data) > index + 1 and value > data[index + 1]:
                    # swap their places
                    data[index], data[index + 1] = data[index + 1], value
                    swapped = True

class TestSort(unittest.TestCase):
    """
    Testing class to test the algorithms in the sort class.
    """
    def test_bubble(self):
        """
        Test that the bubble sort algorithm returns the correct sorted array for the test data.
        """
        data = [2, 4, 1, 5, 9, 3]
        Sort.bubble(data)
        self.assertEqual(data, [1, 2, 3, 4, 5, 9])

if __name__ == '__main__':
    unittest.main()