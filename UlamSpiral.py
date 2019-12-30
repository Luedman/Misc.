import numpy as np
import math
from PIL import Image

# Check if prime
def is_prime(number: int):
    if number > 2:
        for i in range(2,number):
            if (number % i) == 0:
                result = False
                break
            else:
                result = True
    else:
        result = False
    return result


# Create Ulam's Spiral
def ulam_spiral(end_number: int):
    square_length = math.ceil(np.sqrt(end_number))
    if square_length % 2 == 0:
        square_length += 1

    def move_up(x,y):
        return x, y - 1

    def move_down(x,y):
        return x, y + 1

    def move_right(x,y):
        return x + 1, y

    def move_left(x,y):
        return x - 1, y

    test_list_input = [(move_right, 1), (move_up,0), (move_left,1), (move_down,0)]

    def iterate():
        move_list_element = test_list_input.pop(0)
        test_list_input.append(move_list_element)
        return move_list_element
    
    # Initialize
    stepsize = 0
    x,y = (int((square_length - 1)/2), int((square_length - 1)/2))
    grid = np.zeros((square_length,square_length), dtype=np.uint8)
    number = 1

    # Create Spiral
    while number < end_number:
        moving_function, add_to_step = iterate()
        stepsize += add_to_step
        for _ in range(0, stepsize):
            grid[y,x] = is_prime(number)
            number += 1
            x,y = moving_function(x,y)

    # Create Image
    img = Image.fromarray(grid*255)
    img.save("UlamSpiral" + str(end_number) + ".png")
    img.show()

    return grid

    

if __name__ == "__main__":
    ulam_spiral(10000000)




