import nltk
from nltk.corpus import stopwords

# Download the stopwords
nltk.download('stopwords')

# Open files
try:
    with open("file1.txt", "r") as f1, open("file2.txt", "w") as f2:
        # Get the list of English stopwords
        stop = set(stopwords.words("english"))

        # Process each line
        for line in f1:
            words = line.split()
            filtered_words = [word for word in words if word.lower() not in stop]
            f2.write(" ".join(filtered_words) + "\n")
except FileNotFoundError:
    print("One of the files could not be found. Please check the file names.")
except Exception as e:
    print(f"An error occurred: {e}")
