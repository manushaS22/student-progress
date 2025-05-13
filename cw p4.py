# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20222152
# Date: 16/04/2023

print("________________________________________________________ PROGRESS CHECKER _______________________________________________________________")

credits_range=(0,20,40,60,80,100,120)
progress_data = {}

number_of_progress = 0
number_of_trailer = 0
number_of_retriever = 0
number_of_excluded = 0
total_outcomes = 0

repeat_while=True

#progress checking
def check_progress():

    global number_of_progress,number_of_trailer,number_of_retriever,number_of_excluded,total_outcomes
     
    #check total credits equal to 120
    if(total_marks == 120):
        
        #condition for Progress
        if(pass_credit == 120 ):
            print("Progress")
            number_of_progress += 1
            total_outcomes += 1
            return "Progress"

        #condition for Progress(module trailer)
        elif(pass_credit == 100):
            print("Progress (module trailer)")
            number_of_trailer += 1
            total_outcomes += 1
            return "Progress (module trailer)"

        #condition for Exclude
        elif(fail__credit > (pass_credit + defer__credit)):
            print("Exclude")
            number_of_excluded += 1
            total_outcomes += 1
            return "Exclude"

        #condition for Do not progress – module retriever
        else:
            print("Do not progress – module retriever")
            number_of_retriever +=1
            total_outcomes += 1
            return "Do not progress – module retriever"
            

        
    else:
        print("Total incorrect")



print()
version = input("Enter student for student version or staff for staff version : ")

if(version.lower() == "student"):
    while(repeat_while):

        print()
        student_id = input("Please enter your student ID : ")
    
        while(repeat_while):
        
        
            try:
                print()
                pass_credit = int(input("Please enter your credits at pass:"))
                #check pass credits in the credits_range
                if(pass_credit not in credits_range):
                        print("out of range")
                        continue
                
                defer__credit = int(input("Please enter your credit at defer:"))
                #check defer credits in the credits_range
                if(defer__credit not in credits_range):
                        print("out of range")
                        continue
                
                fail__credit = int(input("Please enter your credit at fail:"))
                #check fail credits in the credits_range
                if(fail__credit not in credits_range):
                        print("out of range")
                        continue


            #validate as integer
            except ValueError:
                print("Integer required")
                continue

       
            total_marks = (pass_credit + defer__credit + fail__credit)
        
        
            outcome = check_progress()
            if(outcome == None):
                continue
            else:
                progress_data[student_id] = [pass_credit, defer__credit, fail__credit, outcome]

            repeat_while=False

elif(version.lower() == "staff"):

    #Loop for multiple inputs
    while(repeat_while):

        print()
        student_id = input("Please enter your student ID : ")
        
        while(repeat_while):
        
        
            try:
                print()
                pass_credit = int(input("Please enter your credits at pass:"))
                #check pass credits in the credits_range
                if(pass_credit not in credits_range):
                        print("out of range")
                        continue
                
                defer__credit = int(input("Please enter your credit at defer:"))
                #check defer credits in the credits_range
                if(defer__credit not in credits_range):
                        print("out of range")
                        continue
                
                fail__credit = int(input("Please enter your credit at fail:"))
                #check fail credits in the credits_range
                if(fail__credit not in credits_range):
                        print("out of range")
                        continue


            #validate as integer
            except ValueError:
                print("Integer required")
                continue

       
            total_marks = (pass_credit + defer__credit + fail__credit)
        
        
            outcome = check_progress()
            if(outcome == None):
                continue
            else:
                progress_data[student_id] = [pass_credit, defer__credit, fail__credit, outcome]
        

        
            #Ask for another progress checking
            print()
            control_program = input("To check another student progress press(y) or To quit press(q) :")
            if(control_program.lower() == "y"):
                break
            elif(control_program.lower() == "q"):
                    repeat_while=False
            




print()
print("------------------------------------------------------------------------------")
print()
print("Histogram")
print("Progress {:<3}: {}".format(number_of_progress , '*' * number_of_progress))       #referred in geeksforgeeks.org Available from https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
print("Trailer {:<4}: {}".format(number_of_trailer , '*' * number_of_trailer))          #referred in geeksforgeeks.org Available from https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
print("Retriever {:<2}: {}".format(number_of_retriever , '*' * number_of_retriever))    #referred in geeksforgeeks.org Available from https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
print("Excludes {:<3}: {}".format(number_of_excluded , '*' * number_of_excluded))       #referred in geeksforgeeks.org Available from https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
print()
print(total_outcomes," outcomes in total.")
print()


for student_id, data in progress_data.items():
    print(f"{student_id} : {data[3]} - {data[0]}, {data[1]}, {data[2]}")

print()
print("------------------------------------------------------------------------------")

