# SafeGuardian App
SafeGuardian is a Python application that utilizes the OpenNSFW2 library to analyze image and video content and determine their suitability for children. This application provides a user-friendly interface for users to upload images and videos and receive a safety evaluation based on the NSFW (Not Safe for Work) probability.

## Requirements
Python 3.7 or above
OpenNSFW2 library
Streamlit library

## Installation
* Clone the repository:
```
git clone https://github.com/your-username/safeguardian-app.git
```

* Navigate to the project directory:
```
cd safeguardian-app
```

* Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage
Run the app.py file:
```
python app.py
```

The application will open in your browser.

Upload an image or a video file using the respective file upload buttons.

For image uploads, the application will display the uploaded image along with a safety evaluation indicating whether it is safe or not safe for children. The NSFW probability is shown in parentheses.

For video uploads, the application will display the uploaded video along with a safety evaluation indicating whether it is safe or not safe for children. The NSFW probabilities for each frame of the video are displayed. If any of the probabilities exceed 0.7, the video is considered not safe.

Explore the SafeGuardian app and analyze various images and videos for child safety.


## Acknowledgements
OpenNSFW2 - The library used for NSFW content analysis.
Streamlit - The library used for building the user interface.

Feel free to contribute and make improvements to this project!
