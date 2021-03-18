import streamlit as st
import main
import sklearn
from PIL import Image
import genderanalysis
import ageanalysis

st.title("Do you think you would've survived the Titanic?")
st.write("""
## Please enter your information""")

age = st.number_input("Age", 18)
pclass = st.number_input("Passenger Class", 1, 3)
sibsp = st.number_input("Siblings/Spouses on board", 0)
parch = st.number_input("Parents/Children on board", 0)
sex = st.selectbox(
   'Gender',
   ('Male', 'Female'))
embarked = st.selectbox(
   'Where did you get on the Titanic?',
   ('Southampton', 'Cherbourg', 'Queenstown'))

btn = st.button("See the result")
if sex == 'Male':
    sexN = 1
else:
    sexN = 0

if embarked == 'Southampton':
    embarkedN = 2
elif embarked == 'Queenstown':
    embarkedN = 1
else:
    embarkedN = 0

if btn:
    x = main.model.predict([[pclass, age, sibsp, parch, sexN, embarkedN]])
    if x == 0:
        st.write("Unfortunately, you would not have survived, sorry :(")

        if sexN == 0:
            image = Image.open('C:/Users/Asus/PycharmProjects/TitanicPredictionWebsite/DidYouSurvive/images/sadrose.jpg')
        else:
            image = Image.open('C:/Users/Asus/PycharmProjects/TitanicPredictionWebsite/DidYouSurvive/images/jack.jpg')
        st.image(image, use_column_width=True)
    else:
        st.write("You are a lucky one, congrats!")
        if sexN == 0:
            image = Image.open('C:/Users/Asus/PycharmProjects/TitanicPredictionWebsite/DidYouSurvive/images/rose.png')
        else:
            image = Image.open('C:/Users/Asus/PycharmProjects/TitanicPredictionWebsite/DidYouSurvive/images/happyjack.jpg')

        st.image(image, use_column_width=True)

st.write("""### You can see some of the statistics presented down below """)
st.write("""-Gender based Analysis """)
st.pyplot(genderanalysis.fig)
st.write("""-Age/Class/Embarkment Point based Analysis """)
st.pyplot(ageanalysis.fig)

st.write("""### Some conclusions from the analysis above""")
st.write("From the charts we can see that little less than 40% of the passengers were able to survive"
         " and more than 60% of the survived passengers were female.")
st.write("Around 70% of the passengers embarked in Southampton, and more than 50% of them were in 3rd class.")
st.write("We can also see that the average age of the passengers in 1st class was around 40, and in 3rd class around 20 years of age.")

st.markdown('<hr style="border-top: 10px solid #000000;"/>', unsafe_allow_html=True)
st.write("Thank you for the interest to look at my work!")

link = 'The code for this project is available on my [GitHub.](https://github.com/StankovskiA/DidYouSurviveTheTitanic)'
st.markdown(link, unsafe_allow_html=True)
st.markdown('<hr style="border-top: 10px solid #000000;"/>', unsafe_allow_html=True)
