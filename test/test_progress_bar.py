from easy_deco.progress_bar import ProgressBar
from time import sleep


class Test:

    @ProgressBar(desc='Printing values...', unit='values')
    def show_values(self, value):
        """

        """
        print(value)


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]
    test = Test()
    test.show_values(values)
