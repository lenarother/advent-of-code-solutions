"""Day 3: Toboggan Trajectory

https://adventofcode.com/2020/day/3

"""


def get_input_list_from_file(filename):
    input = open(filename).readlines()
    return list(map(lambda x: x.strip(), input))


class Toboggan:

    def __init__(self, filename):
        self.map = {}
        for counter, line in enumerate(open(filename).readlines()):
            line = line.strip()
            if line:
                self.map[counter] = line
        self.max_x = len(line)
        self.max_y = counter
        self.x = 0
        self.y = 0
        self.trees = 0
        self.count_trees()

    def back_to_start(self):
        self.x = 0
        self.y = 0
        self.trees = 0
        self.count_trees()

    def count_trees(self):
        ch = self.map[self.y][self.x]
        if ch == '#':
            self.trees += 1

    def ride_step(self, r=3, b=1):
        new_x = self.x + r
        if new_x >= self.max_x:
            new_x = new_x % self.max_x
        self.x = new_x
        self.y += b
        self.count_trees()

    def ride(self, r=3, b=1):
        while self.y <= self.max_y - b:
            self.ride_step(r, b)
        return self.trees


def multiple_rides(toboggan, rides):
    result = 1
    for ride in rides:
        trees = toboggan.ride(r=ride[0], b=ride[1])
        result = result * trees
        toboggan.back_to_start()
    return result


if __name__ == '__main__':

    # Part 1
    result = Toboggan('inputdata/day-03-1.txt').ride(3, 1)
    print('Part 1 - Test set 1: ', result)

    result = Toboggan('inputdata/day-03-2.txt').ride(3, 1)
    print('Part 1 - Result: ', result)

    # Part 2
    rides = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    toboggan = Toboggan('inputdata/day-03-1.txt')
    result = multiple_rides(toboggan, rides)
    print('Part 2 - Test set 1: ', result)

    toboggan = Toboggan('inputdata/day-03-2.txt')
    result = multiple_rides(toboggan, rides)
    print('Part 2 - Result: ', result)
