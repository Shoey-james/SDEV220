"""
James Shoemaker
M02_Lab.py
Write a Python app that will accept student names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll. Your app will:
-ask for and accept a student's last name.
-quit processing student records if the last name entered is 'ZZZ'.
-ask for and accept a student's first name.
-ask for and accept the student's GPA as a float.
-test if the student's GPA is 3.5 or greater and, if so, print a message saying that the student has made the Dean's List.
-test if the student's GPA is 3.25 or greater and, if so, print a message saying that the student has made the Honor Roll.
"""
def main():
# define variables
    DEANS_LIST: float = 3.5
    HONOR_ROLL: float = 3.25
    SENTINEL: str = 'ZZZ'
    gpa: float = 0.0
    first_name: str = ''
    last_name: str = ''

# get students last and first name. sentinel input zzz to quit program
    while last_name != SENTINEL:
        last_name = input('Enter last name (ZZZ to quit):')
        if last_name == SENTINEL:
            break
        first_name = input('Enter first name:')
# get student gpa, exception catch for error with value  
        gpa = input('Enter student GPA:')
        try:
            gpa = float(gpa)
        except ValueError:
            print('Invalid input. Please enter numeric value for GPA.')
            continue
# check student gpa against requirements for deans list or honor roll
        if gpa >= 3.5:
            print(f"Great work, {first_name} {last_name}! You are on the Dean's List!")
        elif gpa >= 3.25:
            print(f"Good Job, {first_name} {last_name}! You are on the Honor Roll!")
        else:
            print(f"You did not make Dean's list or honor roll, {first_name} {last_name}! C's get degrees!")
            
# execute main
if __name__ == "__main__":
    main()

    
    
    