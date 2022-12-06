#include <iostream>
#include <Eigen/Dense>
#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/core/eigen.hpp>
#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"

using Eigen::MatrixXd;  // defalut dimension is column
using Eigen::VectorXd;
using Eigen::Matrix3d;
using Eigen::Vector3d;  

/**
 * data structure
 * X: maxtrix(contain squre)
 * i: int
 * d: double
 * f: float
 * c: complex
*/


void eigen_demo()
{
  /**
   * use fixed sizes for very small sizes where you can, and use dynamic sizes for larger sizes or where you have to.
  */
  // matrix
  // MatrixXd m = MatrixXd::Random(3,3);  // dynamic and runtime handle
  Matrix3d m = Matrix3d::Random();
  // m = (m + MatrixXd::Constant(3, 3, 1)) * 2;
  m = (m + Matrix3d::Constant(1)) * 2;
  std::cout << "m =" << std::endl << m << std::endl;

  // comma initial
  Matrix3d m_1;
  m_1 << 1, 2, 3,
         4, 5, 6,
         7, 8, 9;
  std::cout << "m_1 =" << std::endl << m_1 << std::endl;

  // vector
  // vectors are just a special case of matrices
  Vector3d v(1, 2, 3); // dynamic and runtime handle
  std::cout << "m * v =" << std::endl << m * v << std::endl;

}

int cv_to_eigen(cv::Mat img)
{
  // rotate
  /**
   * [[cos\theta, -sin\theta],  [[0.866, -0.5],                       
   *  [sin\theta, cos\theta]]    [0.5, 0.866]]
  */
  // cv::Size size = img.size();
  // cv::Point2i center((int) img.cols / 2, (int) img.rows / 2);
  cv::Point2i center(0, 0);
  cv::Mat cv_rot_mat = cv::getRotationMatrix2D(center, 30, 1.0);
  // std::cout << cv_rot_mat << std::endl;

  // hflip matrix
  cv::Matx23f cv_hflip_mat(-1, 0, img.cols,
                           0,  1, 0);
  // std::cout << cv_hflip_mat << std::endl;
  
  Eigen::MatrixXf eigen_rot_mat;
  cv::cv2eigen(cv_rot_mat, eigen_rot_mat);  // convert cv to eigen
  std::cout << "rotate matrix" << std::endl << eigen_rot_mat << std::endl; 

  Eigen::MatrixXf eigen_hflip_mat;
  cv::cv2eigen(cv_hflip_mat, eigen_hflip_mat); 
  std::cout << "hflip matrix" << std::endl << eigen_hflip_mat << std::endl;
  
  return 0;
  
  // cv::Mat rot_matrix = cv::getRotationMatrix2D();
}
 
int eigen_to_cv(cv::Mat img)
{
  // hflip
  Eigen::Matrix2Xf eigen_vflip_mat(2, 3);
  eigen_vflip_mat << 1, 0, 0, 
                     0,  -1, img.rows;
  cv::Matx23f cv_vflip_mat;
  cv::eigen2cv(eigen_vflip_mat, cv_vflip_mat); // convert eigen to cv
  std::cout << "vflip matrix" << cv_vflip_mat << std::endl;

  // visulize hflip
  cv::Mat vflip_img;
  cv::warpAffine(img, vflip_img, cv_vflip_mat, img.size());
  cv::imshow("origin_img", img);
  cv::imshow("vflip_img", vflip_img);
  cv::waitKey(0);

  return 0;
}

int main()
{
  std::string img_path = TEST_DATA "sunflower.jpg";
  eigen_demo();
  
  cv::Mat img = cv::imread(img_path, cv::IMREAD_COLOR);
  cv_to_eigen(img);
  eigen_to_cv(img);
  
  return 0;
}