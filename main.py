# app.py
import opennsfw2 as n2
import streamlit as st
import statistics

def main():
    st.title("SafeGuardian")
    nsfw_image_list = []
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    video_upload = st.file_uploader("Upload a video", type=["mp4"])
    if uploaded_file is not None:
        # Save the file to a desired location
        with open("uploaded_image.jpg", "wb") as f:
            f.write(uploaded_file.getbuffer())


        # To get the NSFW probability of a single image.
        image_path = "uploaded_image.jpg"

        nsfw_probability = n2.predict_image(image_path)
        if nsfw_probability >= 0.7:
            st.write(f"NOT SAFE ({nsfw_probability:.2f})")
        else:
            st.write(f"SAFE ({nsfw_probability:.2f})")
        # Display the uploaded image
        st.image(uploaded_file)

        # If a video is uploaded
    if video_upload is not None:
        # Save the video to a desired location
        with open("uploaded_video.mp4", "wb") as f:
            f.write(video_upload.getbuffer())

        # To get the NSFW probability of a single video.
        video_path = "uploaded_video.mp4"

        elapsed_seconds, nsfw_probabilities = n2.predict_video_frames(video_path)
        avg_nsfw_prob = statistics.mean(nsfw_probabilities)

        unsafe_frames = []
        for i, p in enumerate(nsfw_probabilities):
            if p >= 0.7:
                unsafe_frames.append(i)

        if unsafe_frames:
            st.write(f"NOT SAFE ({avg_nsfw_prob})")
            # Display the unsafe frames
            for i in unsafe_frames:
                st.image(nsfw_image_list[i], caption=f"Unsafe frame {i}")
        else:
            st.write(f"SAFE ({avg_nsfw_prob})")
            # Display the uploaded video
            st.video(video_upload)


        # if any(nsfw_probabilities) >= 0.7:
        #     st.write(f"NOT SAFE ({avg_nsfw_prob})")
        # else:
        #     st.write(f"SAFE ({avg_nsfw_prob})")
        #     # Display the uploaded video
        #     st.video(video_upload)

if __name__ == '__main__':
    main()