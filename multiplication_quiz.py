import random, time
import pyinputplus as pyip


num_questions = 10
correct_answer = 0
for num in range(num_questions):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print('№ {}: {} x {} = '.format(num + 1, num1, num2))
    try:
        answer = pyip.inputStr(allowRegexes=['{}'.format(num1 * num2)],
                               blockRegexes=[('.*', 'Incorrect!')], timeout=10, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Your answer is correct!')
        correct_answer += 1
    time.sleep(1)

print('Marks: {} / {}'.format(correct_answer, num_questions))
