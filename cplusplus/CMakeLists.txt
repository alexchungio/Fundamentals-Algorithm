cmake_minimum_required(VERSION VERSION 3.0)
project(cplusplus_experiment)


# set variable a value
set(CMAKE_CXX_STANDARD 14)

# all compile define
add_compile_definitions(TEST_DATA="${PROJECT_SOURCE_DIR}/test/data/")

# opencv
find_package(OpenCV REQUIRED) 
include_directories(
    ${OpenCV_INCLUDE_DIR}
)
message("OpenCV library status")
message("   version: ${OpenCV_VERSION}")
message("   include path: ${OpenCV_INCLUDE_DIRS}")
message("   libraries: ${OpenCV_LIBS}")

# eigen
set(Eigen_INCLUDE_DIR "/usr/local/include/eigen3") 
include_directories(
    ${Eigen_INCLUDE_DIR}
)
message("Eigen library status")
message("   include path: ${Eigen_INCLUDE_DIR}")

# add include directories to build
include_directories(
    class
    template
)

# generate share|static library
# add_library(common STATIC util.cpp) 
# add_library(common SHARED util.cpp)

# add subdirectory to build
set(COMMON_LISTS
    class
    interview
    kmp
    leetcode
    linked_list
    struct
    template
    eigen_example
    test)

foreach(COMMON_ITER ${COMMON_LISTS})
    add_subdirectory(${COMMON_ITER})
endforeach(COMMON_ITER)
