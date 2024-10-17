import streamlit as st
import dt.streamlit

def main():
    import streamlit as st
    import smtplib
    import datetime

    # Title of the web app
    st.title("Team Birthday Reminder App")

    # Initialize session state to store user information if not already present
    if "users" not in st.session_state:
        st.session_state.users = []

    # Function to add new user (name, birthdate, email)
    def add_user():
        name = st.session_state["name"]
        birthdate = st.session_state["birthdate"]
        email = st.session_state["email"]

        if name and birthdate and email:
            st.session_state.users.append({"name": name, "birthdate": birthdate.strftime("%Y-%m-%d"), "email": email})
            st.session_state["name"] = ""  # Clear the input boxes
            st.session_state["email"] = ""
            st.success(f"{name} added successfully!")

    # Function to check if today is someone's birthday and send email
    def check_birthdays_and_notify():
        today = datetime.date.today().strftime("%Y-%m-%d")
        birthday_people = [user for user in st.session_state.users if user["birthdate"] == today]

        if birthday_people:
            birthday_person = birthday_people[0]  # Assuming only one birthday per day
            for user in st.session_state.users:
                if user["email"] != birthday_person["email"]:  # Don't email the birthday person
                    send_email(user["email"], birthday_person["name"])
            st.success(f"Birthday emails sent for {birthday_person['name']}!")

    # Function to send email
    def send_email(to_email, birthday_person_name):
        try:
            # Use your email configuration here (example using a Gmail account)
            sender_email = "your_email@gmail.com"
            sender_password = "your_password"
            
            subject = f"🎉 It's {birthday_person_name}'s Birthday Today!"
            message = f"Hi there,\n\nJust a reminder that today is {birthday_person_name}'s birthday! 🎂🎉\n\nDon't forget to wish them!\n\nBest Regards,\nYour Team"
            
            email_text = f"Subject: {subject}\n\n{message}"
            
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, to_email, email_text)
        except Exception as e:
            st.error(f"Error sending email: {e}")

    # Input fields for new users
    st.text_input("Enter your name", key="name")
    st.date_input("Enter your birthdate", key="birthdate")
    st.text_input("Enter your email", key="email")

    # Button to add new user
    st.button("Add to Birthday List", on_click=add_user)

    # Button to check and send birthday notifications
    st.button("Send Birthday Notifications", on_click=check_birthdays_and_notify)

    # Display current list of users
    st.header("Team Members")
    if st.session_state.users:
        for user in st.session_state.users:
            st.write(f"Name: {user['name']}, Birthdate: {user['birthdate']}, Email: {user['email']}")


application = dt.streamlit.Streamlit()

# the app entrypoint makes the app deployable on Datatailr
def __app_main__():
    return application

# this block makes the app runnable in your IDE for debugging purposes
if __name__ == '__main__':
    # feel free to modify the port if 12345 is taken
    application.run(port=12345)