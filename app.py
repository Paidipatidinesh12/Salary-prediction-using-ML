import streamlit as st
st.title("Salary vs Experience")
st.markdown("This ML app will help you predict a software developers salary on the basis of his/her experience")
st.markdown("For example 1 yr 3 months mean 1.03")
x = st.number_input("Enter your years of expericnce in years and months.", 0.0)

def predict():
      y = 9449.96232146*x + 25792.20019867
      return y

if st.button("Let's predict"):
      st.write("You might receive : Rs",round(predict()),"per month")








