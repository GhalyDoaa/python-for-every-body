"""
6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

"""
text = "X-DSPAM-Confidence:    0.8475"
index_of_zero = text.find('0')
print("index_of_zero ",index_of_zero )
#starting search from value of aa =>0
full_number=text[index_of_zero:]
print(full_number)
full_number=float(full_number)
print("full_number",full_number )
