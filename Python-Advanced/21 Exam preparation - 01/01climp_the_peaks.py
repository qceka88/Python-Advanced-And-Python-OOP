from collections import deque


class ClimbThePeaks:
    __peaks_data = {"Vihren": 80,
                    "Kutelo": 90,
                    "Banski Suhodol": 100,
                    "Polezhan": 60,
                    "Kamenitza": 70}

    def __init__(self):
        self.result = []
        self.conquered_peaks = []
        self.food_portions = deque()
        self.stamina = deque()
        self.main_method()

    def main_method(self):
        self.fill_food()
        self.fill_stamina()
        self.start_climbing()
        self.prepare_result()

    def fill_food(self):
        [self.food_portions.append(int(n)) for n in input().split(', ')]

    def fill_stamina(self):
        [self.stamina.append(int(n)) for n in input().split(', ')]

    def start_climbing(self):

        def try_to_climb():
            if current_food + current_stamina >= ClimbThePeaks.__peaks_data[peak]:
                self.conquered_peaks.append(peak)
                return True
            return False

        for peak in ClimbThePeaks.__peaks_data:

            while self.food_portions and self.stamina:
                current_food = self.food_portions.pop()
                current_stamina = self.stamina.popleft()
                if try_to_climb():
                    break
            if not self.food_portions or not self.stamina:
                break

    def prepare_result(self):
        if len(self.conquered_peaks) == len(ClimbThePeaks.__peaks_data):
            self.result.append("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        else:
            self.result.append("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        if self.conquered_peaks:
            self.result.append("Conquered peaks:")
            self.result.extend(self.conquered_peaks)

    def __str__(self):
        return '\n'.join(self.result)


output = ClimbThePeaks()

print(output)