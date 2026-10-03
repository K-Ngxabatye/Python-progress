import pandas as pd

loaded_data = pd.read_csv("phishing_words.csv")
############################################################
#"colour codes for the terminal output"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
RESET = "\033[0m"
############################################################

#logic for scanning the text for potential threats


def scan_threat(text):
    suscount = 0
    sampletext_clean = text.lower()
    suspecious_words = loaded_data["Threat_words"].tolist()

    for susw in suspecious_words:
        if susw in sampletext_clean:
            suscount += 1
             
    suscount_percent = (suscount / len(suspecious_words)) * 100
    
    if suscount > 0:
        print(RED+ "URGENT!!!")                
        print(RED + "FLAGGED AS A POTENTIAL PHISHING SCAM! DO NOT CLICK!!!!" + RESET)
        print(RED + "contact IT department IMMEDIATLY!!!!" + RESET)
        print()
    else: 
        print(GREEN + "No threats have been found, if you see something suspecious or something is not right, please contact IT department, thank you" + RESET)
        print()

    print("-------- Threat analysis --------")
    print()

    if suscount_percent == 0:
        print("Threat score : " + GREEN + str(suscount_percent) + "%" + RESET)
        print("Number of threats : " + str(suscount))
    elif suscount_percent <= 25:
        print("Threat score : " + YELLOW + str(suscount_percent) + "%" + RESET)
        print("Number of threats : " + str(suscount))
    else:
        print("Threat score : " + RED + str(suscount_percent) + "%" + RESET)
        print("Number of threats : " + str(suscount))
    print()
    print("---------------------------------")

#########################################################################################################

#Allows user to input text from a suspected phishing email and scan it for potential threats

scan_threatinput = input(CYAN+"Please enter copied text from work email or suspected threat : "+RESET)
print()
scan_threat(scan_threatinput)

##########################################################################################################

#(UPDATE) Allows user to exit the programme or restart the programme to scan another email or text for potential threats

logout = input(CYAN + "Do you want to stop using the program? y/n? " +RESET)
if logout.lower() == "y":
    print(CYAN+"Thanks for using the  programme, Please make sure you use the programme if you see anything suspecious on your work email" + RESET)
    exit()
elif logout.lower() == "n":
        print(CYAN+"Restarting the programme..." + RESET)
        print()
        scan_threatinput = input(CYAN+"Please enter copied text from work email or suspected threat : "+RESET)
        print()
        scan_threat(scan_threatinput)
else:
        print(RED+ "incorrect input, select \"Y\" OR \"N\"" + RESET)
        
###################################################################################################################################

 # As a result of the update, the programme will now allow the user to scan multiple emails or text for potential threats without having to restart the programme, it also has a logout option which allows the user to exit the programme if they wish to do so
while True:
    logout = input(CYAN + "Do you want to stop using the program? y/n? " +RESET)
    if logout.lower() == "y":
        print(CYAN+"Thanks for using the  programme, Please make sure you use the programme if you see anything suspecious on your work email" + RESET)
        exit()
    elif logout.lower() == "n":
        print(CYAN+"Restarting the programme..." + RESET)
        print()
        scan_threatinput = input(CYAN+"Please enter copied text from work email or suspected threat : "+RESET)
        print()
        scan_threat(scan_threatinput)
    else:
        print(RED+ "incorrect input, select \"Y\" OR \"N\"" + RESET)
#this updated version of the programme allows the user to scan multiple emails or text for potential threats without having to restart the programme, it also has a logout option which allows the user to exit the programme if they wish to do so 
