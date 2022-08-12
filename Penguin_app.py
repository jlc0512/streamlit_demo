import streamlit as st
from PIL import Image


#Header
st.title('Streamlit Demo with Penguins')
st.image('Images/penguins.jpg', use_column_width='always')
st.header('This is a header')
col11, col12 = st.columns(2)
col11.subheader('Column 1')
col12.subheader('Column 2')
col21, col22, col23 = st.columns([3,2,1])
col21.write('widest column which is 3x as big as our smallest column')
col22.write('medium column will wrap around')
col23.write('small column will also wrap around')

st.markdown('Markdown **syntax** *works*')
'Markdown'
'# Magic'
'## A little bit smaller'

st.write('<h2 style="text-align:center"> Text aligned with Html<h2', unsafe_allow_html=True)

st.header('Widget Functionality')

button1 = st.button('This is a button')
if button1:
    st.write('You clicked button')

check1 = st.checkbox('Please check this box')
button2 = st.button('Is box checked')
if button2:
    if check1:
        st.write('The box was checked')
    else:
        st.write('The box was not checked')

st.subheader('Radio Button')
animal_options = ['Cats', 'Dogs', 'Fish']
fav_animal = st.radio('Which animal is your favorite?', animal_options)
button3 = st.button('Submit animal')
if button3:
    st.write(f'You selected {fav_animal} as your favorite animal.')
    if fav_animal == 'Cats':
        st.write('MEOW')
    elif fav_animal == 'Dogs':
        st.write('WOOF')
    else:
        st.write('GULP')

st.subheader('Selectbox')
fav_animal2 = st.selectbox('Which animal is your favorite?', animal_options)
st.write(f'Your favorite animal is {fav_animal2}')

like_animals = st.multiselect('Which animals do you like?', animal_options)
st.write(f'You like {like_animals}')

num_pets = st.slider('How many pets is too many?', 2, 20, 2, 2)
#start at 2, end at 20, count by 2s, default value is 2

pet_name = st.text_input('What is your pets name?', value='I do not have a pet')
st.write(pet_name)

st.sidebar.title('Sidebar')
side_button = st.sidebar.button('Press Me')
if side_button:
    st.write('Button was pressed')

