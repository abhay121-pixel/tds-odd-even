import streamlit as st
st.title('GA 8')
st.subheader('Check if number is ODD or Even')
placeholder_number = st.empty()
n = placeholder_number.number_input('Enter your number')
if float(n)%2 == 0:
	st.write('EVEN Number')
  else:
    st.write('ODD Number')
