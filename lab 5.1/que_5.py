''''
find the position of the word "AI" in the sentence "Machine Learning and AI are trending"
-replace "AI" with "Artificial Intelligence" in the above sentence.
-count how many times the word "data" appears in "data data minimg and big data"
'''

s = "Machine Learning and AI are trending"
print("Position of 'AI' :", s.find("AI"))

n_s = s.replace("AI", "Artificial Intelligence")
print("Replaced sentence:", n_s)

data_text = "data data mining and big data"
print("count of 'data' :", data_text.count("data"))