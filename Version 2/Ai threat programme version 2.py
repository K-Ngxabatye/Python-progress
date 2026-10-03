import pandas as pd

loaded_data = pd.read_csv("phishing_words.csv")

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
RESET = "\033[0m"

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
scan_threatinput = input(CYAN+"Please enter copied text from work email or suspected threat : "+RESET)
print()
scan_threat(scan_threatinput)

#version 2 allows the user to copy text from the suspected physhing scam and paste it on the therminal to check for potential threats
#it also has updated color codes which the IT Department will analyse and see if it is a real risk
#the reason for using colours is to make the user feel as if it is an urgent matter to avoid the user/employee thinking it is a matter that can be avoided
#the current database has words that may be flagged as "threats"
#it is cleaner code 