# Best Enough Guesthouse Booking System (Fixed)

This project contains the updated website and a new backend server to automatically send booking requests to your email.

## 1. Project Structure

*   `index.html`: The main website file (updated to send form data to the server).
*   `app.py`: The new Python backend server (using Flask) that receives booking data and sends the email.
*   `.env`: **CRITICAL** configuration file for your email credentials.
*   The image and video files are the original assets.

## 2. Setup and Configuration (CRITICAL STEP)

The automatic email feature requires a running server and your email credentials.

### A. Configure Email Credentials

You must configure the `.env` file with your email account details. Since you are using Gmail, you **MUST** use an **App Password** instead of your regular password.

1.  **Generate a Gmail App Password:**
    *   Go to your Google Account settings.
    *   Navigate to **Security**.
    *   Under "How you sign in to Google," select **2-Step Verification** (if it's not already on, you must enable it).
    *   Once 2-Step Verification is on, select **App passwords**.
    *   Select **Mail** for the App, and **Other (Custom name)** for the device. Give it a name like "Booking Server".
    *   Click **Generate**. A 16-character password will be displayed. **Copy this password.**

2.  **Update the `.env` file:**
    *   Open the `.env` file in the project folder.
    *   Replace `YOUR_GMAIL_APP_PASSWORD_HERE` with the 16-character App Password you just copied.

    The file should look like this (with your actual App Password):
    ```env
    # --- Email Configuration ---
    # You MUST update these values with your actual email credentials.
    # For Gmail, you need to generate an App Password (not your regular password).
    # See instructions here: https://support.google.com/accounts/answer/185833

    # SMTP Server details
    SMTP_SERVER=smtp.gmail.com
    SMTP_PORT=587

    # Your sending email address (must be a real email account)
    SENDER_EMAIL=bestenoughproperty@gmail.com

    # Your email password or App Password (MANDATORY)
    SENDER_PASSWORD=abcd efgh ijkl mnop
    ```

### B. Install Dependencies

You need to have Python installed on your system. Then, install the required libraries:

```bash
pip install Flask python-dotenv
```

## 3. Running the System

The system has two parts that must be running for the email to be sent: the website and the server.

### A. Start the Backend Server

Open your terminal, navigate to the project directory (`New folder`), and run the server:

```bash
python app.py
```

The server will start and listen on port `5000`. You should see a message like: `Running on http://0.0.0.0:5000/`

**Keep this terminal window open and the server running.**

### B. Open the Website

Open the `index.html` file in your web browser.

Now, when a user fills out the booking form and clicks "Book Now", the website will send the data to the running server, and the server will automatically send the booking details to `bestenoughproperty@gmail.com`.

If the server is not running, the form submission will fail with an alert message.

