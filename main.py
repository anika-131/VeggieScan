import streamlit as st
import tensorflow as tf
import numpy as np

#Tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_model.h5")
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(64,64))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    #convert single image to batch
    input_arr = np.array([input_arr]) 
    predictions = model.predict(input_arr)
    return np.argmax(predictions) 


#Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page",["Home","About Dataset","Prediction"])

#Main Page
if(app_mode=="Home"):
    st.header("VeggieScan")
    image_path = "app\home_img.jpeg"
    st.image(image_path)
    with st.expander("About This Project"):
        st.write("VeggieScan: Simplifying Produce Identification")
        st.caption("Welcome to VeggieScan, an innovative fruits and vegetable recognition system designed to simplify the process of identifying various types of produce. VeggieScan leverages cutting-edge machine learning algorithms to accurately classify images of fruits and vegetables, making it an indispensable tool for consumers, vendors, and educators alike.")
    
        st.write("How It Works")
        st.caption("VeggieScan is equipped to take an image as input and predict its class from a comprehensive set of 36 different fruits and vegetables. Whether you're trying to identify a new type of produce at the market, verifying the contents of a delivery, or educating students about diverse fruits and vegetables, VeggieScan delivers fast and reliable results with just a single click.")


        st.write("Key Features:")
        st.markdown("- Accurate Recognition: Utilizing neural networks, VeggieScan offers high-precision identification, ensuring you get the correct classification every time.")
        st.markdown("- Extensive Database: Our system recognizes 36 different classes of fruits and vegetables, covering a wide range of common and exotic produce.")
        st.markdown("- User-Friendly Interface: With an intuitive and easy-to-use interface, VeggieScan is accessible to users of all ages and technical backgrounds.")
        st.markdown("- Real-Time Processing: Experience quick and efficient recognition with real-time image processing capabilities, perfect for on-the-go use.")

        st.markdown('''
        <style>
        [data-testid="stMarkdownContainer"] ul{
            padding-left:40px;
        }
        </style>
        ''', unsafe_allow_html=True)
    

#About Project
elif(app_mode=="About Dataset"):
    st.header("About The Dataset")
    st.markdown("This dataset is a comprehensive collection of images designed to facilitate the training, testing, and validation of fruit and vegetable recognition systems like VeggieScan. It comprises a total of 3,825 files categorized into 36 distinct classes of fruits and vegetables.")
    st.subheader("Context")
    st.markdown("The dataset includes images of a diverse range of food items:")
    st.markdown("- fruits: banana, apple, pear, grapes, orange, kiwi, watermelon, pomegranate, pineapple, mango.")
    st.markdown("- vegetables: cucumber, carrot, capsicum, onion, potato, lemon, tomato, raddish, beetroot, cabbage, lettuce, spinach, soy bean, cauliflower, bell pepper, chilli pepper, turnip, corn, sweetcorn, sweet potato, paprika, jalepeño, ginger, garlic, peas, eggplant.")
    st.subheader("Content")
    st.markdown("The dataset is organized into three primary folders:")
    st.markdown("- Train: Contains 100 images for each class, used for training the recognition model.")
    st.markdown("- Test: Contains 10 images for each class, used for testing the model's performance.")
    st.markdown("- Validation: Contains 10 images for each class, used for validating the model during development.")
    st.markdown("Each of these folders includes subfolders for each fruit and vegetable class, making it easy to locate and utilize the images for their respective purposes. \nThis structured organization ensures that the dataset is well-suited for developing robust and accurate recognition systems.")

#Prediction Page
elif(app_mode=="Prediction"):
    st.header("Model Prediction")
    test_image = st.file_uploader("Choose an Image:")
    if(st.button("Show Image")):
        st.image(test_image,width=4,use_column_width=True)
    #Predict button
    if(st.button("Predict")):
        st.balloons()
        st.write("Our Prediction")
        result_index = model_prediction(test_image)
        #Reading Labels
        with open("labels.txt") as f:
            content = f.readlines()
        label = []
        for i in content:
            label.append(i[:-1])
        st.success("Model is Predicting it's a {}".format(label[result_index]))