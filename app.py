import streamlit as st
st.title('TDS 8')
st.subheader('Check if number is odd or even')
placeholder_number = st.empty()
m = placeholder_number.number_input('Enter your number')
if float(m)%2 == 0:
	st.write('even number')
else:
 	st.write('odd number')
st.write("Abhaysingh-21f1002151")
