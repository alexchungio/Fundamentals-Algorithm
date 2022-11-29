#include <iostream>
#include <fstream>
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

void image_to_tensor(const std::string filename, const cv::Size & input_size, const cv::Scalar mean, const cv::Scalar std)
{
    int height, width, channels;
    cv::Mat bgr_img, dst_img, tensor_img;
    bgr_img = cv::imread(filename, cv::IMREAD_COLOR);
    // get shape
    std::tie(height, width, channels) = get_shape(bgr_img);
    // resize
    cv::resize(bgr_img, bgr_img, input_size);
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
    cv::subtract(dst_img, mean, dst_img, cv::noArray(), -1);
    // cv::Vec3f pixel_val_sub_mean = dst_img.at<cv::Vec3f>(0, 0);

    // divide std
    cv::divide(dst_img, std, dst_img, 1, -1);
    cv::Vec3f pixel_val_sub_mean_divide_std = dst_img.at<cv::Vec3f>(0, 0);

    // convert to tensor
    // HWC => NCNW
    cv::dnn::blobFromImage(dst_img, tensor_img, 1.0, cv::Size(224, 224));
    
    // verification
    //get (0, 1, 112, 112) => 224 * 224 + 224 * 112 + 112 = 75376 pixel value => 2.1309526
    float * data_ptr = (float *)tensor_img.data;
    float r_0_val = data_ptr[75376];

    cv::imshow("image", bgr_img);
}

// void infile_to_cv(std::string filename)
// {
//     int h, w, max;
//     std::string magic;
//     std::vector<u_int8_t> buffer;
//     std::ifstream infile(filename, std::ifstream::binary);
//     if(infile.is_open())
//     {
//         infile >> magic >> w >> h;
//         infile.seekg(1, infile.cur);
//         // buffer.resize();
//     }
//     cv::waitKey();

// }

void mat_to_array(cv::Mat img)
{
    /*
    typedef const _InputArray& InputArray;
    typedef InputArray InputArrayOfArrays;
    */
    std::vector<cv::Mat> vector_mat = {img};
     // mat -> array
    cv::InputArray img_array = img;
    // array -> mat
    cv::Mat img_mat = img_array.getMat();
    // vector<mat> -> arrayofarray
    cv::InputArrayOfArrays img_vector_array =  vector_mat;
    // arrayofarray -> vector<mat>
    std::vector<cv::Mat> img_vactor_mat;
    img_vector_array.getMatVector(img_vactor_mat);
    
    cv::waitKey(0);
}

void _blob_from_images(cv::InputArrayOfArrays images_, cv::OutputArray blob_, cv::Size size_, 
                       const cv::Scalar& mean_, const cv::Scalar& std_, bool is_bgr_ = false)
{
    // image preprocess
    std::vector<cv::Mat> images;
    images_.getMatVector(images);  // Array to Mat
    CV_Assert(!images.empty());
    for (int i = 0; i < images.size(); i++)
    {
        cv::Size img_size = images[i].size();
        // resize
        if (size_ != img_size)
        {
            resize(images[i], images[i], size_, 0, 0, cv::INTER_LINEAR);
        }
        // convert bgr to rgb
        if(is_bgr_)
        {
            cv::cvtColor(images[i], images[i], cv::COLOR_BGR2RGB);
        }
        // normlize
        if (images[i].depth() == CV_8U)
            images[i].convertTo(images[i], CV_32F, 1.0 / 255.);
        cv::subtract(images[i], mean_, images[i]);
        cv::divide(images[i], std_, images[i]);
        // cv::Vec3f pixel_val_sub_mean_divide_std = images[i].at<cv::Vec3f>(0, 0);
    }

    // convert mat to tensor
    size_t _, num_imgs = images.size();
    int height = images[0].rows;
    int width = images[0].cols;
    int num_chs = images[0].channels();
    cv::Mat blob;
    CV_Assert(images[0].dims == 2);
    CV_Assert(images[0].depth() == CV_32F);
    if (num_chs == 3 || num_chs == 4)
    {
        int blob_size[] = {(int)num_imgs, num_chs, height, width};
        blob_.create(4, blob_size, CV_32F);  // allocate memery
        blob = blob_.getMat();  
        cv::Mat img_chs[4]; 

        for (int i = 0; i < num_imgs; i++)
        {
            cv::Mat image = images[i];
            cv::split(image, img_chs); // split RGB channels
            for (int j = 0; j < num_chs; j++)
            {
                img_chs[j].copyTo(cv::Mat(image.rows, image.cols, CV_32F, blob.ptr((int)i, j)));

            }
        }  
    }
    else
    {
        CV_Assert(num_chs == 1);
        int blob_size[] = {(int)num_imgs, 1, height, height};
        blob_.create(4, blob_size, CV_32F);
        cv::Mat blob = blob_.getMat();
        for (int i = 0; i < num_imgs; i++)
        {
            cv::Mat image = images[i];
            image.copyTo(cv::Mat(image.rows, image.cols, CV_32F, blob.ptr((int)i, 0)));
        }
    }
    // verification
    // get (0, 1, 112, 112) => 224 * 224 + 224 * 112 + 112 = 75376 pixel value => 2.1309526
    float * data_ptr = (float *)blob.data;
    float r_0_val = data_ptr[0];
    cv::waitKey(0);
}

cv::Mat blob_from_images(cv::InputArrayOfArrays images, cv::Size size,
    const cv::Scalar& mean, const cv::Scalar& std_num, bool is_bgr)
{
    cv::Mat blob;
    _blob_from_images(images, blob, size, mean, std_num, is_bgr);

    return blob;
}

int main()
{
    std::string img_path = TEST_DATA "sunflower.jpg";
    const cv::Size input_size = {224, 224};
    const cv::Scalar mean = {0.485f, 0.456f, 0.406f};
    const cv::Scalar std = {0.229f, 0.224f, 0.225f};

    //mat_to_array(img);
    image_to_tensor(img_path, input_size, mean, std);

    // custom image to tensor
    cv::Mat img = cv::imread(img_path);
    auto start = std::chrono::system_clock::now();
    std::vector<cv::Mat> blob_img = {img};
    cv::Mat blob = blob_from_images(blob_img, input_size, mean, std, true);
    auto end = std::chrono::system_clock::now();
    std::cout << std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count() << " ms" << std::endl;

    cv::waitKey();
    
    return 0;
}
