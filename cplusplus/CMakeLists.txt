cmake_minimum_required(VERSION VERSION 2.6)
project(cplusplus_experiment)


# set variable a value
set(CMAKE_CXX_STANDARD 11)
set(Eigen_INCLUDE_DIR "/usr/local/include/eigen3") 

# find external project and load setting
find_package(OpenCV REQUIRED) # opencv

# generate share|static library
# add_library(common STATIC util.cpp) 
# add_library(common SHARED util.cpp)

# all compile define
add_compile_definitions(TEST_DATA="${PROJECT_SOURCE_DIR}/test/data/")

# search for include file
include_directories(
    ${OpenCV_INCLUDE_DIR}
    ${Eigen_INCLUDE_DIR}
    class
    template
)

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
