''' 
import streamlit as st

st.title("My First Streamlit App")
st.write("Hello students, welcome to Streamlit!") '''

# import streamlit as st
# name = st.text_input("Enter your name:")
# st.write("Hello", name)
 
# import streamlit as st
# import pandas as pd

# data = pd.DataFrame({"Marks": [50, 60, 70, 80, 90]})
# st.line_chart(data) '''


# import streamlit as st
# if st.button("Click Me"):
#     st.write("You clicked the button!")

# import streamlit as st
# st.sidebar.button("Click Here")

# st.sidebar.title("Student Controls")
# st.sidebar.title()
# st.sidebar.header()
# st.sidebar.text_input()
# st.sidebar.selectbox()
# st.sidebar.slider()

# import streamlit as st
# st.sidebar.title("Student Controls")

# import streamlit as st
# name = st.sidebar.text_input("Enter your name:")
# st.write("Hello", name)

# import streamlit as st
# subject = st.sidebar.selectbox("Choose Subject", ["Maths", "Science", "English"])
# st.write("You selected:", subject)

# import streamlit as st
# marks = st.sidebar.slider("Select marks", 0, 100)
# st.write("Your marks:", marks)

# import streamlit as st
# st.title("Welcome to My Streamlit App")

# import streamlit as st
# st.header("Student Dashboard")

# import streamlit as st
# st.subheader("Marks Summary")

# import streamlit as st
# st.markdown("# Big Title")
# st.markdown("## Medium Title")
# st.markdown("### Small Title")


# import streamlit as st
# import pandas as pd
# df = pd.read_csv("students.csv")
# st.dataframe(df)

# import streamlit as st
# import pandas as pd
# df = pd.read_csv("students.csv")
# st.header("Student Marks Table")
# st.dataframe(df)
# st.subheader("Average Marks")
# st.write(df[["Maths", "Science", "English"]].mean())


# import streamlit as st
# import pandas as pd
# file = st.file_uploader("Upload CSV file")
# if file:
#     df = pd.read_csv(file)
#     st.dataframe(df)

# import streamlit as st
# import pandas as pd
# df = pd.read_csv("students.csv")
# st.line_chart(df[["Maths", "Science", "English"]])

#### **Example 1: Remove missing rows**
# import streamlit as st
# import pandas as pd
# df = pd.read_csv("data.csv")
# clean_df = df.dropna()
# st.dataframe(clean_df)

#### **Example 2: Fill missing values**
# import streamlit as st
# import pandas as pd
# df = pd.read_csv("data.csv")
# df["Marks"] = df["Marks"].fillna(0)
# st.dataframe(df)

#### **Example 3: Remove duplicate rows**
# import streamlit as st
# import pandas as pd
# df = pd.read_csv("data.csv")
# df = df.drop_duplicates()
# st.dataframe(df)

#### **Example 4: Fix data format**
# import streamlit as st
# import pandas as pd
# df = pd.read_csv("data.csv")
# df["Name"] = df["Name"].str.strip()
# st.dataframe(df)


#### **Example 1: Simple Linear Regression in Streamlit**

# import streamlit as st
# import pandas as pd
# from sklearn.linear_model import LinearRegression

# st.title("Simple Salary Prediction App")

# # Read CSV
# df = pd.read_csv("salary.csv")

# st.subheader("Salary Dataset")
# st.dataframe(df)

# # Model
# model = LinearRegression()
# model.fit(df[["Experience"]], df["Salary"])

# # Input
# exp = st.number_input("Enter Experience (in years):", 1, 50)

# # Prediction
# pred = model.predict([[exp]])

# st.subheader("Predicted Salary")
# st.write(int(pred[0]))

#### **Example 2: Training + Chart**

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("Salary Prediction with Chart")
df = pd.read_csv("salary.csv")

model = LinearRegression()
model.fit(df[["Experience"]], df["Salary"])

st.line_chart(df.set_index("Experience"))

exp = st.slider("Experience (Years)", 1, 15)
pred = model.predict([[exp]])

st.write("Predicted Salary:", int(pred[0]))

