import cv2

video = "fish.mp4"
output = "images/"

vidcap = cv2.VideoCapture(video)  # Create a video capture object
count = 0  # Initialize frame count

# Read the first frame
success, image = vidcap.read()

num_frames = 100
every_x_frame = 100

while success:
    if count % every_x_frame == 0:
        cv2.imwrite(output + "frame%d.jpg" % count, image)
    success, image = vidcap.read()  # Read the next frame

    # Increment frame count
    count += 1

    if count >= every_x_frame * num_frames:
        break

# Release the video capture object
vidcap.release()
