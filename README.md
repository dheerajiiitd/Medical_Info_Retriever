# Medical-Information-Retrival-System

# Disease Detection based on Symptoms
Information Retrival (CSE 508) Project
Medical information retrieval system 

# Introduction
This project uses novel techniques of Machine learning and IR techniques to detect diseases based on symptoms and provide more details about the top fetched diseases including treatment recommendation.

The model which performed best was  LR(logistic regression) & SVM (Support Vector Machine) with an accuracy of 92.99% and 92.53%, with cross validation of LR is 89.19% and SVM is 88.62%.

The system can be used by a person with restricted medical knowledge as well with ease and can come handy in early disease detection and diagnosis. It can also benefit users that are reluctant to visit hospitals on the onset of minor symptoms. This will provide them with a basic idea of the severity of the disease.

# Background
Machine Learning applications in healthcare and biomedical domain has lead to early disease detection and better diagnosis. Studies have shown that people take the help of the internet for any possible health-related issues. The problem with this approach is that the search engines provide bulk information in scattered format from which it is difficult to conclude.

There are many disease prediction systems available such as heart disease prediction, neurological disorders prediction, and skin disease prediction. But universal prediction system for diseases based on symptoms is rarely in practice. It is very helpful for doctors and patients to know better about the disease without any medical tests or anything else.

The detection of disease based on disease is a complex game. Being unfamiliar with biological terms, the users feed the symptoms in non-technical or natural terms which add complexity in predicting diseases.

# Dataset used

The previously available dataset is restricted to a particular part of human body disease and is also smaller in volume. Hence, the dataset of disease and their symptoms has been scraped from the web by running the Python script. The dataset consists of diseases and their symptoms, which are fetched from the following sources:

**Diseases**: The list of diseases has been retrieved from the National Health Portal of India ( https://www.nhs.uk/conditions/), developed and maintained by Crown. The script fetches the HTML code of the page and extracts the disease list by filtering values in HTML tags.

**Symptoms**: The script uses the Google Search package to perform searching and fetch the disease’s Wikipedia page among the various search results obtained. The HTML code of the page is processed to fetch the symptoms of the disease using the ’infobox’ available on the Wikipedia page.

The scraping script fetches over all different diseases that form the label and 500+ symptoms and some manual work is also done over the list of diseases.

# Running the system

Either run **Final_file.ipynb** to use the system. **Google Colab is recommended** for running the system as it uses googlesearch library to suggest treatments, it was observed to be throwing error in Kaggle and Pycharm IDE.

# Results

Evaluation of the dataset is done by applying various machine learning algorithms and comparing the accuracy obtained from them. The **highest accuracy is reported by LR(logistic regression) 92.99% & SVM (Support Vector Machine) with an accuracy of 92.53%.

The system’s performance is evaluated by comparing the predicted diseases that were obtained by the proposed system with the one obtained from Mayoclinic(https://www.mayoclinic.org/diseases-conditions) or WebMD’s Symptom Checker Module ( https://symptoms.webmd.com/default.htm ) and it showed somewhat similar results.

#Evaluations

Comparison of baseline and  current system performance
in the baseline result, we tested the or model on the data, which gives the highest accuracy of up to 85.75% with MNB. Now, we modified our system by increasing the data and adding more evaluation matrices, and we got an accuracy of 92.99% with logistic regression and  99.53% with the Support vector machine.


SOTA on different evaluation matrices And the handling of different cases:
In our existing project, we take input from the user, perform lemmatization of the user's input, and then search for the top 10 diseases. Based on this, we suggest the treatment to the user. We handle different cases by symptom-matching of diseases provided by user. This is being achieved after performing Synonym Expansion, Similarity Check, Selection promt, Related Symptom discovery and Iterative suggestions where commonly co-occuring symptoms are presented iteratively for user selection

# Contributions

Project came into reality_ by [Shreeram kumar singh](shreeram23091@iiitd.ac.in), [Mohit singh tanwar](Mohit23127@iiitd.ac.in) and [Dheeraj pandey](dheeraj23034@iiitd.ac.in) and [Nitesh kumar chaurasia](nitesh23053@iiitd.ac.in), [Tanmay Parashar](tanmay23100@iiitd.ac.in) and [Shubham kumar choudhary](shubham23093@iiitd.ac.in)

