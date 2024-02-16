import streamlit as st
import time

# Set the page config to wide mode for better layout
st.set_page_config(layout="wide")

# Title for app
st.title('5 Minute Timer with Sequential Messages & Calculators')
st.write('This app will display a timer counting down from 5 minutes. With two minutes left it will say to "Add Marker in Omnia", at one minute left it will say to "Get RPE and Awkwardness", and at 30 seconds left it will say to "Start Recording in MotionMonitor". At the bottom there are calculators that will take number of steps taken in 15 seconds to step rate per minute, and calcualte 105% and 110% of that value. 90% and 110% of preferred gait speed will also be calculated.')
st.write('This is meant as a guide for data collection for the CADENCE Study.')
st.write('---')
st.title('Calculators')
gs = st.number_input("Input the preferred gait speed value.")
if gs >0:
    below = round(gs*.9,2)
    above = round(gs*1.1,2)
    cooldown = round(gs*.6,2)
    column1,column2,column3,column4 = st.columns(4)
    column1.metric('10% Below PGS',str(below))
    column2.metric('PGS',str(gs))
    column3.metric('10% Above PGS',str(above))
    column4.metric('60% Of PGS (Easy Walking)',str(cooldown))

numval = st.number_input("Input the number of steps taken in 15 seconds")
if numval >1:
    full = round(numval*4)
    sixty = round((numval*.6*4))
    onefive = round((numval*1.05*4))
    oneone = round((numval*1.1*4))

    col2,col3,col4 = st.columns(3)
    col2.metric('Step Rate: 100%',str(full))
    col3.metric('Step Rate: 105%',str(onefive))
    col4.metric('Step Rate: 110%',str(oneone))


st.write('---')
st.title('Timer')
# Create a start button
if st.button('Start Timer'):

    # Create an empty placeholder for the timer
    timer_placeholder = st.empty()
    # Create an empty placeholder for Omnia
    omnia_message_placeholder = st.empty()
    # Create an empty placeholder for RPE
    rpe_message_placeholder = st.empty()
    # Create an empty placeholder for MM
    mm_message_placeholder = st.empty()

    # Set the countdown time (5 minutes)
    countdown = 300  # 300 seconds for 5 minutes

    # Start the countdown
    for i in range(countdown, 0, -1):
        # Format the timer
        mins, secs = divmod(i, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)

        # Update the timer placeholder with the current timer value
        timer_placeholder.markdown(f"# Time Remaining: {timer}")

        # When there are 2 minutes left, display "Add Marker in Omnia"
        if i == 120:  # 120 seconds is equal to 2 minutes
            omnia_message_placeholder.markdown("## -Add Marker in Omnia")

        # When there is 1 minute left, display "Get RPE & Awkwardness"
        elif i == 60:  # 60 seconds is equal to 1 minute
            rpe_message_placeholder.markdown("## --Get RPE & Awkwardness")

        # When there are 30 seconds left, display "Start Recording in Motion Monitor"
        elif i == 30:  # 30 seconds
            mm_message_placeholder.markdown("## ---Start Recording in Motion Monitor")

        # Wait for 1 second before updating the timer
        time.sleep(1)

    # Once the countdown is over, display the message
    timer_placeholder.markdown("### Timer Ended! On to the next trial!")
st.write('---')

st.write('Written by Dante Goss')