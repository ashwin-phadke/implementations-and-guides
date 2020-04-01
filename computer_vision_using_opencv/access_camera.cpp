#include "opencv2/opencv.hpp"
#include <iostream>

using namespace std;
using namespace cv;

int main(){

  // Invoke VideoCapture method by passing camera ID arguement from user

  VideoCapture cap(0); 
   
  // Check to see if the camera opens up and if it doesn't raise appropriate error
  if(!cap.isOpened()){
    cout << "Error opening video stream or file" << endl;
    return -1;
  }
	
  // While camera is opened
  while(1){

    Mat frame;
    
    cap >> frame;
 
    // If the frame is empty, break immediately
    if (frame.empty())
      break;

    //  Display the result
    imshow( "Frame", frame );

    // Press  ESC on keyboard to exit
    char c=(char)waitKey(25);
    if(c==27)
      break;
  }
 
  // Check to see if escape key was pressed every defined time interval and break if pressed
  cap.release();

  destroyAllWindows();
	
  return 0;
}
