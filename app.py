import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Rock vs Mine", layout="wide")

st.title("Prediction whether the object is a mine or rock")
st.text("")
st.text("")
st.text("In the Following 60 number inputs, Enter the 60 atributes in the range of 0.00 to 1.00 which represents the energy in a particular Frequency Band.")
st.text("After Entering the inputs Click on the Submit button to get the Output.")
st.text("")
st.text("")

para_1, para_2, para_3, para_4, para_5, para_6 = st.columns(6)
para_7, para_8, para_9, para_10, para_11, para_12 = st.columns(6)
para_13, para_14, para_15, para_16, para_17, para_18 = st.columns(6)
para_19, para_20, para_21, para_22, para_23, para_24 = st.columns(6)
para_25, para_26, para_27, para_28, para_29, para_30 = st.columns(6)
para_31, para_32, para_33, para_34, para_35, para_36 = st.columns(6)
para_37, para_38, para_39, para_40, para_41, para_42 = st.columns(6)
para_43, para_44, para_45, para_46, para_47, para_48 = st.columns(6)
para_49, para_50, para_51, para_52, para_53, para_54 = st.columns(6)
para_55, para_56, para_57, para_58, para_59, para_60 = st.columns(6)


c1 = para_1.number_input("Enter The 1st Parameter")
c2 = para_2 .number_input("Enter The 2nd Parameter")
c3 = para_3 .number_input("Enter The 3rd Parameter")
c4 = para_4 .number_input("Enter The 4th Parameter")
c5 = para_5 .number_input("Enter The 5th Parameter")
c6 = para_6 .number_input("Enter The 6th Parameter")
c7 = para_7 .number_input("Enter The 7th Parameter")
c8 = para_8 .number_input("Enter The 8th Parameter")
c9 = para_9 .number_input("Enter The 9th Parameter")
c10 = para_10.number_input("Enter The 10th Parameter")
c11 = para_11.number_input("Enter The 11th Parameter")
c12 = para_12.number_input("Enter The 12th Parameter")
c13 = para_13.number_input("Enter The 13th Parameter")
c14 = para_14.number_input("Enter The 14th Parameter")
c15 = para_15.number_input("Enter The 15th Parameter")
c16 = para_16.number_input("Enter The 16th Parameter")
c17 = para_17.number_input("Enter The 17th Parameter")
c18 = para_18.number_input("Enter The 18th Parameter")
c19 = para_19.number_input("Enter The 19th Parameter")
c20 = para_20.number_input("Enter The 20th Parameter")
c21 = para_21.number_input("Enter The 21th Parameter")
c22 = para_22.number_input("Enter The 22th Parameter")
c23 = para_23.number_input("Enter The 23th Parameter")
c24 = para_24.number_input("Enter The 24th Parameter")
c25 = para_25.number_input("Enter The 25th Parameter")
c26 = para_26.number_input("Enter The 26th Parameter")
c27 = para_27.number_input("Enter The 27th Parameter")
c28 = para_28.number_input("Enter The 28th Parameter")
c29 = para_29.number_input("Enter The 29th Parameter")
c30 = para_30.number_input("Enter The 30th Parameter")
c31 = para_31.number_input("Enter The 31th Parameter")
c32 = para_32.number_input("Enter The 32th Parameter")
c33 = para_33.number_input("Enter The 33th Parameter")
c34 = para_34.number_input("Enter The 34th Parameter")
c35 = para_35.number_input("Enter The 35th Parameter")
c36 = para_36.number_input("Enter The 36th Parameter")
c37 = para_37.number_input("Enter The 37th Parameter")
c38 = para_38.number_input("Enter The 38th Parameter")
c39 = para_39.number_input("Enter The 39th Parameter")
c40 = para_40.number_input("Enter The 40th Parameter")
c41 = para_41.number_input("Enter The 41th Parameter")
c42 = para_42.number_input("Enter The 42th Parameter")
c43 = para_43.number_input("Enter The 43th Parameter")
c44 = para_44.number_input("Enter The 44th Parameter")
c45 = para_45.number_input("Enter The 45th Parameter")
c46 = para_46.number_input("Enter The 46th Parameter")
c47 = para_47.number_input("Enter The 47th Parameter")
c48 = para_48.number_input("Enter The 48th Parameter")
c49 = para_49.number_input("Enter The 49th Parameter")
c50 = para_50.number_input("Enter The 50th Parameter")
c51 = para_51.number_input("Enter The 51th Parameter")
c52 = para_52.number_input("Enter The 52th Parameter")
c53 = para_53.number_input("Enter The 53th Parameter")
c54 = para_54.number_input("Enter The 54th Parameter")
c55 = para_55.number_input("Enter The 55th Parameter")
c56 = para_56.number_input("Enter The 56th Parameter")
c57 = para_57.number_input("Enter The 57th Parameter")
c58 = para_58.number_input("Enter The 58th Parameter")
c59 = para_59.number_input("Enter The 59th Parameter")
c60 = para_60.number_input("Enter The 60th Parameter")


model = joblib.load('sonar_rock_vs_mines_detection.pkl')

x = np.array([
    c1,
    c2,
    c3,
    c4,
    c5,
    c6,
    c7,
    c8,
    c9,
    c10,
    c11,
    c12,
    c13,
    c14,
    c15,
    c16,
    c17,
    c18,
    c19,
    c20,
    c21,
    c22,
    c23,
    c24,
    c25,
    c26,
    c27,
    c28,
    c29,
    c30,
    c31,
    c32,
    c33,
    c34,
    c35,
    c36,
    c37,
    c38,
    c39,
    c40,
    c41,
    c42,
    c43,
    c44,
    c45,
    c46,
    c47,
    c48,
    c49,
    c50,
    c51,
    c52,
    c53,
    c54,
    c55,
    c56,
    c57,
    c58,
    c59,
    c60,
])

st.write(" ")
st.write(" ")
st.write(" ")

b1, b2, b3, b4, b5, b6 = st.columns(6)


if b4.button('Submit'):
    try:
        ans = model.predict([x])[0]
        if ans == 'R':
            st.success("According to the Model its a Rock")
        else:
            st.success("According to the Model its a Mine")
    except:
        st.error("Something went Wrong, Please Check your Parameters")
    