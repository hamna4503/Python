"""3.   Write Python expressions corresponding to these statements:
(a)The number of characters in the word "anachronistically" is 1
 more than the number of characters in the word "counterintuitive."""
print(len("anachronistically")==(len("counterintuitive")+1))

# (b)The word "misinterpretation" appears earlier in the dictionary
# than the word "misrepresentation."
print("misinterpretation"<"misrepresentation")

#(c)The letter "e" does not appear in the word "ﬂoccinaucinihilipiliﬁcation."
print("e" not in "ﬂoccinaucinihilipiliﬁcation")

#(d)The number of characters in the word counterrevolution"
# is equal to the sum of the number of characters in words "counter" and "resolution."
print(len("counterrevolution")== len("counter")+len("resolution"))