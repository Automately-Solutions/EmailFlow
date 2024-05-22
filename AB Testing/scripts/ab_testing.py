import csv
import random
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from abba import ABBA

# Ensure nltk vader_lexicon is downloaded
import nltk
nltk.download('vader_lexicon')

# Email contents for A/B testing
email_content_A = input("Enter the content for Email A: ")
email_content_B = input("Enter the content for Email B: ")

# Load email list
email_list_file = 'data/email_list.csv'
email_results_file = 'data/email_results.csv'

def load_email_list(file_path):
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

def save_email_result(file_path, results):
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Email", "Email_Type", "Sentiment"])
        for result in results:
            writer.writerow(result)

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    return sentiment

def main():
    email_list = load_email_list(email_list_file)
    results = []

    for entry in email_list:
        recipient_email = entry["Email"]
        recipient_name = entry["Name"]

        # Randomly choose between email content A and B
        chosen_content = email_content_A if random.choice([True, False]) else email_content_B
        email_type = 'A' if chosen_content == email_content_A else 'B'

        sentiment = analyze_sentiment(chosen_content)
        print(f"Email {email_type} assigned to {recipient_email} with sentiment {sentiment}")
        results.append([recipient_email, email_type, sentiment])

    save_email_result(email_results_file, results)

    # Prepare data for ABBA analysis
    email_a_count = len([result for result in results if result[1] == 'A'])
    email_b_count = len([result for result in results if result[1] == 'B'])

    abba = ABBA()
    abba.fit(results)
    abba.summary()

if __name__ == "__main__":
    main()