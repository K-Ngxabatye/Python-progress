import pandas as pd

loaded_data = pd.read_csv("phishing_words.csv")
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
def scan_threat(text):
    suscount = 0
    sampletext_clean = text.lower()
    suspecious_words = loaded_data["Threat_words"].tolist()
#logic
    for susw in suspecious_words:
        if susw in sampletext_clean:
             suscount +=1         
    suscount_percent = suscount/len(suspecious_words)*100
    
    if suscount > 0:
        print(RED+"FLAGGED AS A POTENTIAL PHISHING SCAM! DO NOT CLICK!!!!"+RESET)
        print(RED+"contact IT department IMMEDIATLY!!!!"+RESET)
        print()
    else: 
        print(GREEN+"No threats have been found, if you see something suspecious or something is not right, please contact IT department, thank you"+RESET)
        print()
    print("-------- Threat analysis --------")
    print()
    if suscount_percent >=25:
        print("Threat score : " + Yellow + str(suscount_percent)+"%"+RESET)
        print("Number of threats : " +str(suscount))
    else:
        print("Threat score : " + GREEN + str(suscount_percent)+"%"+RESET)
        print("Number of threats : " +str(suscount))
        print()
    print()
    print("---------------------------------")
scan_threat("congrats, you are a winner")