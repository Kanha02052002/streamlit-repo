import streamlit as sl

sl.title("Hi, I am Streamlit App ")
sl.subheader("Hi, I am Kanha ")
sl.header("I am Header")
sl.text("Text Function")

# MARKDOWN

sl.markdown("**HELLO** *World*")
sl.markdown("# h1 Tag")
sl.markdown("[Youtube](https://www.youtube.com/ )")

sl.markdown("---")
# Captions

sl.caption("Hi, I am NoxRe")

# mathametical Expression

sl.latex(r"\begin{pmatrix}a&b\\c&b\\e&f\end{pmatrix}")

# json Function => work as expander as of now -> can copy elements

json={
    "a":"1,2,3",
    "b":"4,5,6",
}
sl.json(json)

# code funtion
code="""
    import os
    print("OS module is imported")
"""
sl.code(code)
sl.code(code,"python")