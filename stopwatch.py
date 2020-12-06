import time


# описание класса-секундомера
class Stopwatch:

    def __init__(self, num_runs):
        self.time_amount = 0
        self.time_start = 0
        self.num_runs = num_runs

    def __call__(self, func):
        def wrapper():
            for i in range(self.num_runs):
                print(str(i+1) + ' try...')
                self.time_start = time.time()
                func()
                self.time_amount += time.time() - self.time_start
            self.time_amount /= self.num_runs
            print('Average time: %.5f' % self.time_amount)
        return wrapper

    def __enter__(self):
        self.time_start = time.time()
        print('Start...')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.time_amount = time.time() - self.time_start
        print('Average time: %.5f' % self.time_amount)


# Количество измерений выполнения программы
NUM_RUNS = 3


# Тестовая функция с классом-декоратором
@Stopwatch(NUM_RUNS)
def say_hello_and_w8():
    print('Hello user!')
    time.sleep(1)


def main():

    # Вызов функции с классом-декоратором
    say_hello_and_w8()

    # Использование класса в качестве контекствного менеджера
    with Stopwatch(NUM_RUNS):
        time.sleep(3)


if __name__ == '__main__':
    main()
