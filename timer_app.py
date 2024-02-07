import streamlit as st
import time

# Set the page config to wide mode for better layout
st.set_page_config(layout="wide")

# Title for app
st.title('5 Minute Timer with Sequential Messages')
st.write('This app will display a timer counting down from 5 minutes. With two minutes left it will say to "Add Marker in Omnia", at one minute left it will say to "Get RPE and Awkwardness", and at 30 seconds left it will say to "Start Recording in MotionMonitor"')
st.write('This is meant as a guide for data collection for the CADENCE Study.')
st.write('---')

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
st.write('Calculator')
numval = st.number_input("Input a Number",min_val = 0)
ninety = round((numval*.9))
onefive = round((numval*1.05))
oneone = round(numval*1.1)

col1,col2,col3,col4 = st.columns(4)
col1.metric('Ninety Percent',ninety.as.str())
st.write('---')
st.write('Written by Dante Goss')