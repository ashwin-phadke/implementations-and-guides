import cv2
import argparse

# FUnction to access camera using camera ID provided by the user
def access_camera(cam_id):
    """
    cam_id : camera ID obtained from user.
    """
    # Invoke VideoCapture method by passing camera ID arguement from user
    cap = cv2.VideoCapture(cam_id)
    
    # Check to see if the camera opens up and if it doesn't raise appropriate error
    if not cap.isOpened():
        raise IOError("Cannot access camera, please check if you entered the ID correctly")

    # While camera is opened
    while True:

        # Read the camera input
        """
        ret : return True if the frame is available from the camera reading operation below.
        frame : array of frames as it loops.
        """
        ret, frame = cap.read()

        # Resizing window to save resources and have defined window
        cv2.resize(frame, (640,480))

        fps = cv2.VideoCapture.get(CV_CAP_PROP_FPS)
        print(fps)
        # Display the result
        cv2.imshow("output", frame)

        # Check to see if escape key was pressed every defined time interval and break if pressed
        check = cv2.waitKey(1)
        if check == 27:
            break

    # Release the camera resource   
    cap.release()

    # Destroy all windows
    cv2.destroyAllwindows()


if __name__ == "__main__":

    # Implement argparse to accept command line arguements to choose methods.
    parser = argparse.ArgumentParser(description='This program let you access camera by ID')

    # Access the camera by ID provided by the user.
    parser.add_argument('--cam_id', type=int, help='Camera ID')

    args = parser.parse_args()

    # Function call to access_camera for Video Capture
    access_camera(cam_id=args.cam_id)