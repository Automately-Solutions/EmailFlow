from textblob import TextBlob

def analyze_sentiment(email):
    """
    Analyze the sentiment of the email content.
    
    :param email: The content of the email.
    :return: Sentiment polarity and subjectivity.
    """
    analysis = TextBlob(email)
    return analysis.sentiment

def compare_emails(email_a, email_b):
    """
    Compare the sentiment of two emails.
    
    :param email_a: The content of email A.
    :param email_b: The content of email B.
    """
    sentiment_a = analyze_sentiment(email_a)
    sentiment_b = analyze_sentiment(email_b)
    
    print("Email A Sentiment:")
    print(f"  Polarity: {sentiment_a.polarity}")
    print(f"  Subjectivity: {sentiment_a.subjectivity}\n")
    
    print("Email B Sentiment:")
    print(f"  Polarity: {sentiment_b.polarity}")
    print(f"  Subjectivity: {sentiment_b.subjectivity}\n")
    
    if sentiment_a.polarity > sentiment_b.polarity:
        print("Email A has a more positive sentiment than Email B.")
    elif sentiment_a.polarity < sentiment_b.polarity:
        print("Email B has a more positive sentiment than Email A.")
    else:
        print("Both emails have the same sentiment polarity.")

def main():
    email_a = input("Enter the content of Email A: ")
    email_b = input("Enter the content of Email B: ")
    
    compare_emails(email_a, email_b)

if __name__ == "__main__":
    main()
