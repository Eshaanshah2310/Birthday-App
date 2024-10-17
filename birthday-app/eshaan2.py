import streamlit as st
import dt.streamlit

def main():
    import streamlit as st
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

        if name and birthdate:
            st.session_state.users.append({"name": name, "birthdate": birthdate.strftime("%Y-%m-%d")})
            st.session_state["name"] = ""  # Clear the input boxes
            st.success(f"{name} added successfully!")

    # Function to check if today is someone's birthday and show notification
    def check_birthdays():
        today = datetime.date.today().strftime("%Y-%m-%d")
        birthday_people = [user for user in st.session_state.users if user["birthdate"] == today]

        if birthday_people:
            for person in birthday_people:
                st.success(f"🎉 It's {person['name']}'s Birthday Today! 🎂")

    # Input fields for new users
    st.text_input("Enter your name", key="name")
    st.date_input("Enter your birthdate", key="birthdate", min_value=datetime.date(1965, 1, 1))

    # Button to add new user
    st.button("Add to Birthday List", on_click=add_user)

    # Button to check for birthdays
    st.button("Check Today's Birthdays", on_click=check_birthdays)

    # Display current list of users
    st.header("Team Members")
    if st.session_state.users:
        for user in st.session_state.users:
            st.write(f"Name: {user['name']}, Birthdate: {user['birthdate']}")



application = dt.streamlit.Streamlit()

# the app entrypoint makes the app deployable on Datatailr
def __app_main__():
    return application

# this block makes the app runnable in your IDE for debugging purposes
if __name__ == '__main__':
    # feel free to modify the port if 12345 is taken
    application.run(port=12345)