

import re
from googlesearch import search
import warnings
warnings.filterwarnings("ignore")
import requests
from bs4 import BeautifulSoup

# Take input a disease and return the content of wikipedia's infobox for that specific disease
def diseaseDetail(term):
    diseases=[term]
    ret=term+"\n"
    info_dict = {}
    for dis in diseases:
        # search "disease wilipedia" on google
        query = dis+' wikipedia'
        for sr in search(query,tld="co.in",stop=10,pause=0.5):
            # open wikipedia link
            match=re.search(r'wikipedia',sr)
            filled = 0
            if match:
                wiki = requests.get(sr,verify=False)
                soup = BeautifulSoup(wiki.content, 'html5lib')
                # Fetch HTML code for 'infobox'
                info_table = soup.find("table", {"class":"infobox"})
                if info_table is not None:
                    # Preprocess contents of infobox
                    for row in info_table.find_all("tr"):
                        data=row.find("th",{"scope":"row"})
                        if data is not None:
                            symptom=str(row.find("td"))
                            symptom = symptom.replace('.','')
                            symptom = symptom.replace(';',',')
                            symptom = symptom.replace('<b>','<b> \n')
                            symptom=re.sub(r'<a.*?>','',symptom)
                            symptom=re.sub(r'</a>','',symptom)
                            symptom=re.sub(r'<[^<]+?>',' ',symptom)
                            symptom=re.sub(r'\[.*\]','',symptom)
                            symptom=symptom.replace("&gt",">")
                            ret+=data.get_text()+" - "+symptom+"\n"
                            info_dict[data.get_text()]=symptom
                            #print(data.get_text(),"-",symptom)
                            filled = 1
                if filled:
                    break
    return info_dict

diseases_input=input("Enter the disease name:\t")
info_dict=diseaseDetail(diseases_input)

def print_treatment():
  flag=0
  for key, value in info_dict.items():
    if(key =="Treatment"):
      flag=1
      print(f"{key}: {value}")
    if(key =="Diagnostic method"):
      flag=1
      print(f"{key}: {value}")
    if(key =="Differential diagnosis"):
      flag=1
      print(f"{key}: {value}")
    if(key =="Medication"):
      flag=1
      print(f"{key}: {value}")
  return flag

def scrape_disease_info(disease_name):
    url = f"https://en.wikipedia.org/wiki/{disease_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Finding the sections containing treatment, diagnostic methods, and medications
    treatment_section = soup.find("span", id="Treatment")
    diagnostic_section = soup.find("span", id="Diagnosis")
    medication_section = soup.find("span", id="Medications")

    # Extracting text from the sections if found
    treatment_info = treatment_section.find_next("p").text if treatment_section else "Information not found."
    diagnostic_info = diagnostic_section.find_next("p").text if diagnostic_section else "Information not found."
    medication_info = medication_section.find_next("p").text if medication_section else "Information not found."

    return {
        "Treatment": treatment_info,
        "Diagnostic methods": diagnostic_info,
        "Medications": medication_info
    }

returned_flag = print_treatment()
if(returned_flag == 0):
  disease_info = scrape_disease_info(diseases_input)
  if(disease_info["Treatment"] != "Information not found."):
    print("Treatment:", disease_info["Treatment"])
  if(disease_info["Diagnostic methods"]!="Information not found."):
    print("Diagnostic methods:", disease_info["Diagnostic methods"])
  if(disease_info["Medications"] != "Information not found."):
    print("Medications:", disease_info["Medications"])



