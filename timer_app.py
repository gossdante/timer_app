import streamlit as st
import time

# Set the page config to wide mode for better layout
st.set_page_config(layout="wide")

# Title for your app
st.title('5 Minute Timer with Sequential Messages')


# Create a start button
if st.button('Start Timer'):

    # Create an empty placeholder for the timer
    timer_placeholder = st.empty()
    # Create an empty placeholder for messages
    message_placeholder = st.empty()

    # Set the countdown time (5 minutes)
    countdown = 300  # 300 seconds for 5 minutes

    # Start the countdown
    for i in range(countdown, 0, -1):
        # Format the timer
        mins, secs = divmod(i, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)

        # Update the timer placeholder with the current timer value
        timer_placeholder.markdown(f"### Time Remaining: {timer}")

        # When there are 2 minutes left, display "Add Marker in Omnia"
        if i == 120:  # 120 seconds is equal to 2 minutes
            message_placeholder.markdown("### Add Marker in Omnia")
        if i == 115:
            message_placeholder.empty()
        # When there is 1 minute left, display "Get RPE & Awkwardness"
        elif i == 60:  # 60 seconds is equal to 1 minute
            message_placeholder.markdown("### Get RPE & Awkwardness")

        # When there are 30 seconds left, display "Start Recording in Motion Monitor"
        elif i == 30:  # 30 seconds
            message_placeholder.markdown("### Start Recording in Motion Monitor")

        # Wait for 1 second before updating the timer
        time.sleep(1)

    # Once the countdown is over, display the message
    timer_placeholder.markdown("### Timer Ended!")
    # Clear the special message
    message_placeholder.empty()


import streamlit as st

# Title for your app
st.title('Streamlit App with Beep Sound')

# Add a button to trigger the beep
if st.button('Click me to beep'):
    # Embed an audio file
    audio_file = 'beep-08b.mp3'  # Replace with the path to your audio file

    # Create the HTML to embed the audio
    audio_html = f"""
    <audio autoplay>
    <source src="{audio_file}" type="audio/mpeg">
    Your browser does not support the audio element.
    </audio>
    """

    # Display the audio
    st.markdown(audio_html, unsafe_allow_html=True)

