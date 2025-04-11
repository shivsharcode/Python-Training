import nltk

nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

text_token = nltk.word_tokenize("My name is Shivam")

pos = nltk.pos_tag(text_token)
print(pos)

"""
{
    "input_text" : "content" ,
    "rephrased_text_response" : "content"
}
"""


"""
FINAL ?

{
    {
        "input_text" : "content" ,
        "rephrased_text_response" : "content"
    }
    {
        "input_text" : "content" ,
        "rephrased_text_response" : "content"
    }
    ..........
}
    
"""