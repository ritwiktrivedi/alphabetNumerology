import streamlit as st

# supporting functions

alpha_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13,
              "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}


def numfunc(someText):
    tsum = 0
    for i in someText:
        if i.isalpha():
            i = i.lower()
            tsum += alpha_dict[i]
    return tsum


def nsum(tsum):
    tsum = str(tsum)
    nsum = 0
    for i in tsum:
        nsum += int(i)
    return nsum

# app code


st.title("Alphabet Numerology App")
st.write(
    "This is a simple app to find the sum of alphabets!"
)


title = st.text_input("Write the name here:", "Write here")
st.write(f"The sum of alphabets in [{title}] is", numfunc(title))

st.write(f"The reduced sum or the sum of numbers in sum is", nsum(numfunc(title)))
