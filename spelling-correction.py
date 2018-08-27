# Get vocabulary to use
vocabulary = open("dictionnaire.txt","r",encoding = "utf-8").read()
tokenized_vocabulary = vocabulary.split(' ')

# get text to corect
data = open("texte.txt","r",encoding = "utf-8").read()
data =  data.replace('.','').replace(',','').replace('\n','').replace("''",'')

# clean the text from all specials caracters
def clean_text(string, clean_caracters, replacement_string):
    cleaned_value = string
    for clean_caracter in clean_caracters:
        cleaned_value =  cleaned_value.replace(clean_caracter,replacement_string)
    return cleaned_value.lower()

# tokenisation of text
def tokenize(string, clean_caracters, replacement_string, must_clean = False):
    cleaned_value = string
    if must_clean:
        cleaned_value = clean_text(string, clean_caracters, replacement_string)
    return cleaned_value.split(' ')

# correction ortographique"       
def spell_check(vocabulary_file,data_file,specialCaracters = [",",".","'","\n","(",")","!"],replacement_string=""):
    data = open(data_file,"r",encoding = "utf-8").read()
    vocabulary = open(vocabulary_file,"r",encoding = "utf-8").read()
    tokenize_data =  tokenize(data,specialCaracters,replacement_string, must_clean = True)
    tokenize_vocabulary =  tokenize(vocabulary,specialCaracters,replacement_string)
    
    misspelled_words = []
    for token in tokenize_data:
        if token not in tokenized_vocabulary and token !='':
            misspelled_words.append(token)
    return misspelled_words

# print misspelled words 
final_misspelled_word = spell_check(vocabulary_file = "dictionnaire.txt",data_file = "texte.txt")        
print(final_misspelled_word)