class Calculator:
    count = 0

    @staticmethod
    def add(a, b):
        Calculator.count += 1
        return a + b

print(Calculator.add(3, 4))
print("Add function called:", Calculator.count, "times")
