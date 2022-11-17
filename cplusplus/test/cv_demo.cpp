#include <iostream>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>

using namespace std;

int main(){
    std::string img_path = TEST_DATA "sunflower.jpg";
    cv::Mat bgr_img = cv::imread(TEST_DATA "sunflower.jpg");
    cv::imshow("image", bgr_img);
    cv::waitKey(0);
    
    return 0;
}