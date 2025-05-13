# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20221198
# Date: 16/04/2023

print("________________________________________________________ PROGRESS CHECKER _______________________________________________________________")

credits_range=(0,20,40,60,80,100,120)
Progress_list =[]
module_trailer_list =[]
Module_retriever_list =[]
Exclude_list =[]
progress_type = ""

number_of_progress = 0
number_of_trailer = 0
number_of_retriever = 0
number_of_excluded = 0
total_outcomes = 0

repeat_while=True

#progress checking
def check_progress():

    global number_of_progress,number_of_trailer,number_of_retriever,number_of_excluded,total_outcomes,progress_type

    #check total credits equal to 120
    if(total_marks == 120):
        
        #condition for Progress
        if(pass_credit == 120 ):
            print("Progress")
            number_of_progress += 1
            total_outcomes += 1
            progress_type = "Progress"
            Progress_list.append(pass_credit)
            Progress_list.append(defer__credit)
            Progress_list.append(fail__credit)
            file_save()

        #condition for Progress(module trailer)
        elif(pass_credit == 100):
            print("Progress (module trailer)")
            number_of_trailer += 1
            total_outcomes += 1
            progress_type = "Progress (module trailer)"
            module_trailer_list.append(pass_credit)
            module_trailer_list.append(defer__credit)
            module_trailer_list.append(fail__credit)
            file_save()
            
        #condition for Exclude
        elif(fail__credit > (pass_credit + defer__credit)):
            print("Exclude")
            progress_type = "Exclude"
            number_of_excluded += 1
            total_outcomes += 1
            Exclude_list.append(pass_credit)
            Exclude_list.append(defer__credit)
            Exclude_list.append(fail__credit)
            file_save()
            

        #condition for Do not progress – module retriever
        else:
            print("Do not progress – module retriever")
            number_of_retriever +=1
            total_outcomes += 1
            progress_type = "Do not progress – module retriever"
            Module_retriever_list.append(pass_credit)
            Module_retriever_list.append(defer__credit)
            Module_retriever_list.append(fail__credit)
            file_save()

        
    else:
        print("Total incorrect")

#part 2
#print progression and credits using list
def print_progress_level(progression,which_list):
    for i in range(0, len(which_list), 3):
        credit_items = which_list[i:i+3]
        print(progression , ','.join(str(x) for x in credit_items))     #referred in www.w3schools.com Available from https://www.w3schools.com/python/ref_string_join.asp

#part 3
#function for saving to file(marks.txt)
def file_save():
    f=open('marks.txt','a')
    f.write('{}{}{},{},{}\n'.format(progress_type," - ",pass_credit,defer__credit,fail__credit))
    f.close()


f=open('marks.txt','w')
f.write("Entered credits\n")
f.close()



print()
version = input("Enter student for student version or staff for staff version : ")

if(version.lower() == "student"):
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
        #run the progress checking
        check_progress()
        repeat_while=False


    
elif(version.lower() == "staff"):


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
        #run the progress checking
        check_progress()
       
        

        #Ask for another progress checking
        print()
        control_program = input("To check another student progress press(y) or To quit press(q) :")
        if(control_program.lower() == "y"):
            continue
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

#part 2
print("part 2\n")
print_progress_level("Progress - ",Progress_list)                       
print_progress_level("module trailer - ",module_trailer_list)
print_progress_level("Module retriever - ",Module_retriever_list)
print_progress_level("Exclude - ",Exclude_list)
print()

#part 3
print("part 3\n")
f=open('marks.txt')
lines=f.readlines()

for line in lines[1:]:
    line=line.strip()
    print(line)
f.close()

print()
print("------------------------------------------------------------------------------")



