#include <iostream>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/dnn.hpp>

using namespace std;

template <typename T>
cv::Vec<T, 3> get_pixel_value(T* img_ptr, int cols, int channels, int x, int y)
{
    cv::Vec<T, 3> pixel_val;
    
    pixel_val[0] = img_ptr[(y * cols + x) * channels + 0];
    pixel_val[1] = img_ptr[(y * cols + x) * channels + 1];
    pixel_val[2] = img_ptr[(y * cols + x) * channels + 2];

    return pixel_val; 
}

std::tuple<int, int, int> get_shape(cv::Mat image)
{   
    // (height, width, channels)
    int height = image.rows;
    int width = image.cols;
    int channels = image.channels();

    return std::make_tuple(height, width, channels);
     
}

void image_to_tensor(std::string filename, const int input_size[2], const float mean[3], const float std[3])
{
    int height, width, channels;
    cv::Mat bgr_img, dst_img, tensor_img;
    bgr_img = cv::imread(filename, cv::IMREAD_COLOR);
    // get shape
    std::tie(height, width, channels) = get_shape(bgr_img);
    // resize
    cv::resize(bgr_img, bgr_img, cv::Size(input_size[0], input_size[1]));
    // bgr to rgb
    cv::cvtColor(bgr_img, dst_img, cv::COLOR_BGR2RGB);
    // cv::Vec3b pixel_val_0 = dst_img.at<cv::Vec3b>(0, 0);  // (y, x)
    // cv::Vec<uint8_t, 3> pixel_val_0 = get_pixel_value((u_int8_t *)dst_img.data, 
    //                                                   width, channels, 0, 0);

    /** image normalize
    (2, 54, 85)
    (2 / 255, 54 / 255, 85 / 255) => (0.00784313772， 0.211764723， 0.333333343)
    (0.00784313772 - 0.485， 0.211764723 - 0.456， 0.333333343 - 0.406) => (-0.477156878, -0.244235277, -0.0726666451)
    (-0.477156878 / 0.229, -0.244235277 / 0.224, -0.0726666451 / 0.225) => (-2.0836544, -1.09033608, -0.32296288)
    */
    //  normalize
    dst_img.convertTo(dst_img, CV_32FC3, 1.0 / 255.);
    // cv::Vec3f pixel_val_norml = dst_img.at<cv::Vec3f>(0, 0);
    // cv::Vec<float, 3> pixel_val_norml = get_pixel_value((float *)dst_img.data, 
    //                                                     width, channels, 0, 0);
    // substract mean 
    cv::subtract(dst_img, cv::Scalar(mean[0], mean[1], mean[2]), dst_img, cv::noArray(), -1);
    // cv::Vec3f pixel_val_sub_mean = dst_img.at<cv::Vec3f>(0, 0);

    // divice std
    cv::divide(dst_img, cv::Scalar(std[0], std[1], std[2]), dst_img, 1, -1);
    // cv::Vec3f pixel_val_sub_mean_divide_std = dst_img.at<cv::Vec3f>(0, 0);

    // convert to tensor
    // HWC => NCNW
    cv::dnn::blobFromImage(dst_img, tensor_img, 1.0, cv::Size(224, 224));
    auto c = tensor_img.size().height;

    cv::imshow("image", bgr_img);
}

int main(){
    std::string img_path = TEST_DATA "sunflower.jpg";
    const int input_size[2] = {224, 224};
    const float mean[3] = {0.485f, 0.456f, 0.406f};
    const float std[3] = {0.229f, 0.224f, 0.225f};
    // cv::Mat bgr_img = cv::imread(TEST_DATA "sunflower.jpg");
    // cv::imshow("image", bgr_img);
    // cv::waitKey(0);
    image_to_tensor(img_path, input_size, mean, std);
    return 0;
}