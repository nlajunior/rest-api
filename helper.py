import pandas as pd
import string

def count_25(data):
    values = data.values
    max_value = max(data)
    max_index = data[data==max_value]
    count_max_index = max_index.value_counts() 
    return max_value, count_max_index[max_value]

def get_alphabet():
    ascii_values = string.ascii_uppercase
    alphabet = [] 
    for letter in ascii_values:
        alphabet.append(letter)
    alphabet = pd.Series(range(0,26),index=alphabet)
    return alphabet

alphabet = get_alphabet()   

def get_letter_by_position(position):
    return alphabet[alphabet==position].index[0]

def get_letter(last_letter):
    return alphabet[last_letter]

def word_to_number(word, n_digits):
    count = 0
    last_word = pd.Series([0]*n_digits)
    for digit in word:
        last_word[count] = get_letter(digit)
        count = count+1
    return last_word

def get_validate_digit(id_digits):
    return sum(id_digits)%26

def new_sum(data, n_digits):
    n_digits_api=4
    
    if n_digits==n_digits_api: #API
        value_data = data
        max_serie_number = n_digits
        max_count = n_digits+1  
    else: #Local
        value_data = data[0:n_digits]
        max_serie_number = n_digits-1
        max_count = n_digits
        
    # Count ocurrence of 25 
    max_value, number_25 = count_25(value_data)
        
    # Create dict of values by position
    values_by_position = pd.Series([0]*max_serie_number)
    values_by_position[max_serie_number] = 1
    

    # Create dict sum of values by position and the data
    sum_values = values_by_position + value_data
    
    # Adjust dict to threshold of 25 (Letter Z=25 and A=0)
    if max_value==25:
        if number_25<max_count:
            for i in reversed(range(max_count)):
                if sum_values[i]>=26 and i>0:
                    sum_values[i] = sum_values[i]-26
                    if sum_values[i-1]<26:
                        sum_values[i-1] = sum_values[i-1]+1
        else:
            sum_values = data
            print('No more DIGITS') 
    
    if n_digits==n_digits_api: #API
        return_sum_value = sum_values
        
    else: #Local
        sum_values[n_digits] = get_validate_digit(sum_values) 
        return_sum_value = sum_values
     
    return return_sum_value

def get_id_monitoring(n_samples, last_id):
    n_digits = 0
    for letter_in_id in last_id:
        n_digits = n_digits+1
    x = n_digits-1   
    last_data = word_to_number(last_id, x)

    # Create number of letters id list
    list_number_ids = []
    for i in range(0,n_samples):
        data = new_sum(last_data, n_digits-1)
        list_number_ids.append(data)
        last_data = data
        
    # Translate number of letters id list to letter id list
    list_of_ids = []
    for value in list_number_ids:
        letters = []
        for number in value:
            letters.append(get_letter_by_position(number))
        letters_form = "".join(letters)
        list_of_ids.append(letters_form)
    return list_of_ids[0]

