# By Kami Bigdely
# Decompose conditional
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age

# Blood test analysis program

class Levels:
    def __init__(self, good, high):
        self.good = good
        self.high = high

    def is_high(self, result):
        if result >= self.high:
            return True
        return False

    def is_good(self, result):
        if result < self.good:
            return True
        return False


TOTAL_CHOLESTEROL = Levels(200, 240)
LDL = Levels(100, 160)
TRIGLYCERIDES = Levels(150, 200)


class Bloodwork:

    def __init__(self, total_cholesterol, ldl, triglycerides):
        self.tc = total_cholesterol
        self.ldl = ldl
        self.trig = triglycerides

    def levels_high(self):
        return TOTAL_CHOLESTEROL.is_high(self.tc) or LDL.is_high(self.ldl) or TRIGLYCERIDES.is_high(self.trig)

    def levels_good(self):
        return TOTAL_CHOLESTEROL.is_good(self.tc) and LDL.is_good(self.ldl) and TRIGLYCERIDES.is_good(self.trig)

    def show_TLC_diet(self):
        print("\nStart TLC diet")
        print(" - Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
        print(' - Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
        print(' - oats, barley, and other whole grains.')
        print(' - fruits such as apples, pears, bananas, and oranges.')

    def summary(self):
        if self.levels_high():
            print('*** High cholestrol level ***')
            print('start taking pills such as statins')
            self.show_TLC_diet()
        elif self.levels_good():
            print('*** Good level of cholestrol ***')
        else:
            print('Error: unhandled case.')


tc = 70
ldl = 30
trig = 120
Bloodwork(tc, ldl, trig).summary()
