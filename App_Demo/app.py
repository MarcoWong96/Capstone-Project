import streamlit as st
import pandas as pd
import joblib
import numpy as np
import shap
import matplotlib.pyplot as plt

# Load your trained model
loaded_model = joblib.load('final_model.pkl')  
loaded_scaler = joblib.load('scaler.pkl') 
import_train_df = pd.read_csv('app_dataframe.csv')

# Set title
st.title("Projecting Player Valuation using Statistics")

# Descriptor
st.write('''This application will predict a football player's valuation. 
This model has been derived from a gradient boosting algorithm, combined with Recursive Feature Engineering, 
on player statistics datasets from the 2021 to 2023 seasons. 
The valuations modelled against is directly from TransferMarkt. 
\n\nTo use this model, please adjust the statistics on the left to the required levels. Currently, all
the default values are set at the mean(average).''')

# Set X_train_select
df_columns = ['Comp_Premier League', 'Team_Middle', 'Team_Top', 'Age', 'Starts',
       '90s', 'Goals', 'Shots', 'PasTotCmp%', 'PasMedCmp%', 'SCA',
       'ScaPassLive', 'GCA', 'TouAtt3rd', 'TouAttPen', 'TouLive', 'Rec',
       'Recov', 'AerWon', '2023']

# Data Dictionary
# Define and display the data dictionary
data_dictionary = {
    'Comp_Premier League': 'Whether the player plays in the Premier League (1 if true, 0 if false)',
    'Team_Middle': 'Whether the player belongs to a middle-tier team (1 if true, 0 if false)',
    'Team_Top': 'Whether the player belongs to a top-tier team (1 if true, 0 if false)',
    '2023': 'Whether it is the year 2023 (1 if true, 0 if false)',
    'Age': 'The age of the player',
    '90s': 'Number of 90-minute intervals the player participated in',
    'Starts': 'Number of games the player started',
    'Goals': 'Number of goals scored by the player per 90',
    'GCA': 'Goal creating actions by the player',
    'Rec': 'Number of times a player successfully received a pass',
    'SCA': 'Shot creating actions by the player',
    'AerWon': 'Number of aerial duels won by the player',
    'ScaPassLive': 'Shot creating actions from live passes',
    'Shots': 'Number of shots taken by the player per 90',
    'PasTotCmp%': 'Pass completion percentage of total passes',
    'TouAtt3rd': 'Number of ball touches in the attacking third',
    'TouAttPen': 'Number of ball touches in the penalty area',
    'TouLive': 'Number of live ball touches',
    'Recov': 'Number of loose balls recovered',
}

# Function to scale user_data
def scale_user_input(user_input):
    # Create a DataFrame with original column names
    user_input_df = pd.DataFrame(user_input, columns=df_columns)
    
    # Scale user input using the loaded scaler
    scaled_input = loaded_scaler.transform(user_input_df)
    return scaled_input

def main():
    st.title('Player Valuation Predictor')

    # Collect user input
    st.sidebar.title('Player Statistics')

    # Display checkbox title
    st.sidebar.write('Check if applies')

    # Create checkboxes for binary features
    feature3 = st.sidebar.checkbox('Plays in Premier League? (Comp_Premier League)')
    feature4 = st.sidebar.checkbox('Plays for Mid Table club? (Team_Middle)')
    feature5 = st.sidebar.checkbox('Plays for Top Table club? (Team_Top)')
    feature20 = st.sidebar.checkbox('Valuation in 2023? (2023)')

    # Display input sliders
    st.sidebar.write('Slider scale')

    # Convert specific slider values to floats for step=0.5
    feature1 = st.sidebar.slider('Age', min_value=18, max_value=41, value=26)
    feature6 = st.sidebar.slider('Number of 90 Minutes completed (90s)', min_value=0, max_value=38, value=11)
    feature2 = st.sidebar.slider('Starts', min_value=0, max_value=38, value=11)
    feature7 = st.sidebar.slider('Goals per 90 (Goals)', min_value=0.0, max_value=1.5, value=0.5, step = 0.1)
    feature13 = st.sidebar.slider('Goal Creating Actions per 90 (GCA)', min_value=0.0, max_value=4.0, value=0.2, step=0.5)
    feature17 = st.sidebar.slider('Balls received (Rec)', min_value=0, max_value=100, value=30)
    feature11 = st.sidebar.slider('Shot Creating Actions per 90 (SCA)', min_value=0.0, max_value=5.0, value=2.0, step=0.5)
    feature19 = st.sidebar.slider('Total Aerials Won (AerWon)', min_value=0.0, max_value=5.0, value=1.5, step=0.5)
    
    feature12 = st.sidebar.slider('Shot Creating Actions from Live passes per 90 (ScaPassLive)', min_value=0.0, max_value=5.0, value=1.4, step=0.2)
    feature8 = st.sidebar.slider('Shots per 90 (Shots)', min_value=0.0, max_value=3.0, value=1.2, step = 0.1)
    feature9 = st.sidebar.slider('Pass completion Percentage (PasTotCmp%)', min_value=0, max_value=100, value=80)
    feature10 = st.sidebar.slider('Medium pass completion percentage (PasMedCmp%)', min_value=0, max_value=100, value=80)
    feature14 = st.sidebar.slider('Touches in Attacking Third (TouAtt3rd)', min_value=0, max_value=30, value=15)
    feature15 = st.sidebar.slider('Touches in Offensive Penalty area (TouAttPen)', min_value=0, max_value=10, value=2)
    feature16 = st.sidebar.slider('Live ball touches (TouLive)', min_value=0, max_value=100, value=51)
    feature18 = st.sidebar.slider('Recoveries (Recov)', min_value=0, max_value=30, value=6)


    # Create a callback for live updates
    @st.cache_data()
    def predict_valuation(user_input):
            scaled_user_input = scale_user_input(user_input)
            prediction = loaded_model.predict(scaled_user_input)
            return prediction

    #Create a DataFrame with the user input
    user_input = np.array([1 if feature3 else 0, 1 if feature4 else 0, 1 if feature5 else 0,
                           feature1, feature2, feature6, feature7, feature8, feature9,
                           feature10, feature11, feature12, feature13, feature14, feature15,
                           feature16, feature17, feature18, feature19, 1 if feature20 else 0]).reshape(1, -1)

    #Set scaled_user_data variable
    scaled_user_input = scale_user_input(user_input)

    # Display the prediction
    st.success('## Predicted Valuation: {:.1f} Million €'.format(np.round(np.exp(predict_valuation(user_input)[0])/1_000_000, 1)))

    # Write description
    st.write('The below graph shows the effect of each statistic on the players valuation.')
    
    # Function to generate SHAP plot
    def generate_shap_plot(user_input):
        explainer = shap.Explainer(loaded_model, import_train_df)
        shap_values = explainer.shap_values(scaled_user_input)

        # Create a summary plot of SHAP values
        fig, ax = plt.subplots()
        shap.summary_plot(shap_values, features=user_input, feature_names=df_columns, show=False)
        st.pyplot(fig)

    generate_shap_plot(scaled_user_input)  # Initial SHAP plot based on default values


    # Use Streamlit's "st.slider" to detect changes in the slider values
    # if st.button('Update SHAP Plot'):
    #    user_input = np.array([1 if feature3 else 0, 1 if feature4 else 0, 1 if feature5 else 0,
    #                           feature1, feature2, feature6, feature7, feature8, feature9,
    #                           feature10, feature11, feature12, feature13, feature14, feature15,
    #                           feature16, feature17, feature18, feature19, 1 if feature20 else 0]).reshape(1, -1)

    #    scaled_user_input = scale_user_input(user_input)

     #   generate_shap_plot(scaled_user_input)  # Update SHAP plot on button click
    
    # Put Data Dictionary
    st.write('### Data Dictionary')
    for feature, description in data_dictionary.items():
        st.write(f"- **{feature}:** {description}")
if __name__ == "__main__":
    main()




