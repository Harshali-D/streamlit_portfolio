import streamlit as st
from PIL import Image
# Set the background image for the whole website
# Create the header section
st.title("Harshali Deshmukh Portfolio !")
st.write("Welcome to my portfolio website!")
# Create the "My Projects" section
st.header("Below are my projects!")

st.markdown("<h3 style='border: 2.5px solid white; border-radius: 10px; padding: 10px; margin-bottom: 20px;'> 1) Stock Market Prediction Model</h3>", unsafe_allow_html=True)

# Set the background image
stock_market = Image.open("C:/Users/harsahli/Desktop/stock_market_model.jpg")
st.image(stock_market, use_column_width=True)

st.markdown(f"[Click here to open](https://drive.google.com/file/d/13SZCyptx497j3_JqORHscRitgHxF0wa5/view?usp=sharing)")
st.write("This project is about predicting the stock market in real time. \n"
         "It uses a variety of machine learning techniques to analyze stock market data and make predictions about the next day stock prices.\n "
         "user simple has to chose their ticker and wait for it to predict next days price \n "
         "it can predict 1) Crypto\n "
         "2) ALL the index of the world\n "
         "3) All the comodities of the world\n"
         "3) Any cryptocurrency and NFT\n "
         "4) Prices of forex ")



st.markdown("<h3 style='border: 2.5px solid white; border-radius: 10px; padding: 10px; margin-bottom: 20px;'> 2) Automatic Email Sender</h3>", unsafe_allow_html=True)
# Set the background image
email_img = Image.open("C:/Users/harsahli/Desktop/email_sender.jpg")
st.image(email_img, use_column_width=True)

st.markdown(f"[Click here to open](https://drive.google.com/file/d/1igpohH11zfAqndM9nxImGeMJ5xB3xwkX/view?usp=sharing)")
st.write("This is a mini project i did for my organization , when often there is need of regular follow up from the client\n T"
         "his program allows the user to repeat sending a the email after a specified duration\n "
         "It can be done as many times as one wishes , It can also often doubled as an elaborate prank on my friends to flood their inbox with 600 emails in 60 seconds")

st.markdown("<h3 style='border: 2.5px solid white; border-radius: 10px; padding: 10px; margin-bottom: 20px;'> 3) Netflix Power Bi dashboard </h3>", unsafe_allow_html=True)

# Set the background image
netflix = Image.open("C:/Users/harsahli/Desktop/All dashboard projects/netflix_dashboard.png")
st.image(netflix, use_column_width=True)
st.markdown(f"[Click here to open](https://drive.google.com/file/d/1Sh4BIbkTfc4nWx8T7gLbly1K4z6vJKuv/view?usp=sharing)")
st.write("A Dashboard is a valuable tool for understanding the company's performance.\n"
         " This dashboard provides insights into the company's financial performance, subscriber base, content library, marketing efforts, and technology platform. \n"
         "The data is presented in both tabular and graphical form, making it easy to see trends and changes over time")


st.markdown("<h3 style='border: 2.5px solid white; border-radius: 10px; padding: 10px; margin-bottom: 20px;'> 4) Amazon Sales Insight Tableau Dashboard  </h3>", unsafe_allow_html=True)

# Set the background image
amazon = Image.open("C:/Users/harsahli/Desktop/All dashboard projects/Screenshot 2023-08-16 145129.png")
st.image(amazon, use_column_width=True)

st.markdown(f"[Click here to open](https://drive.google.com/file/d/1I76UUU2JIsapK0dctIk1DCrHo6jPStbd/view?usp=sharing)")
st.write("The visualization provides insights into clothing sales data for Amazon. \n"
         "The data is presented in a variety of ways, including bar charts, line charts, and heat maps.\n"
         "Overall, the visualization provides a wealth of insights into sales data for Amazon.\n"
         " The data allows viewers to quickly and easily see the information they are looking for.")




st.markdown("<h3 style='border: 2.5px solid white; border-radius: 10px; padding: 10px; margin-bottom: 20px;'> 5) Movie Recommendation System</h3>", unsafe_allow_html=True)

# Set the background image
amazon = Image.open("C:/Users/harsahli/Desktop/pexels-nathan-engel-436413.jpg")
st.image(amazon, use_column_width=True)

st.markdown(f"[Click here to open](https://drive.google.com/drive/folders/1Tx99DaUWL2MykUU1GZAka0iyl2RQWGJ8?usp=sharing)")
st.write("This is a basic movie reccommendation system  \n"
         "The model contains more than 4900 movies to let the user chose from \n"
         "When one movie is selected by the the user , the model suggest 5 more similar movies \n"
         "Movies that the user is sure to enjoy.")




# Create the "My Resume" section
st.markdown("<h2 style='border: 2.5px solid white; border-radius: 10px; padding: 10px; margin-bottom: 20px;'>My Resume</h2>", unsafe_allow_html=True)
with open("C:/Users/harsahli/Desktop/Harshali Deshmukh.pdf", "rb") as f:
    st.download_button("Download resume here", f, file_name="Harshali_Deshmukh.pdf")


# Create the "My Contact Info" section
st.markdown("<h3 style='border: 2.5px solid white; border-radius: 10px; padding: 10px; margin-bottom: 20px;'> My contact Information</h3>", unsafe_allow_html=True)
st.write("Name: Harshali Bhushan Deshmukh")
st.write("Adress : 411045 Maharashtra , India")
st.write("Email: harshali982002@gmail.com")
st.write("Phone: +91 8669601532")




st.write("Thank you for visiting my portfolio website!")
