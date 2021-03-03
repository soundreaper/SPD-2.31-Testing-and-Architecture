# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math


def print_banner(mean, sd):
    # print out the mean and standard deviation in a nice format.
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')


def calculate_grades(grade_list):
    # Calculate the mean and standard deviation of the grades
    grade_total = 0
    for grade in grade_list:
        grade_total += grade
    # calculate the mean
    mean = grade_total / len(grade_list)

    # calculate standard deviation
    sd = 0  # standard deviation
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list))

    return sd, mean


def get_grades():
    # placeholder grade list to add user input
    grade_list = []
    # get the aomount of students to calculate grades for
    n_student = int(input("How many students do you have? "))
    # get the grades
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))

    return grade_list


def print_stat():
    # get the grade list from the user
    grade_list = get_grades()
    # calculate the grades
    sd, mean = calculate_grades(grade_list)

    # print the banner with the final grades
    print_banner(mean, sd)


print_stat()
