cmake_minimum_required(VERSION VERSION 2.6)
project(cplusplus_experiment)

# set cmaker standard
set(CMAKE_CXX_STANDARD 11)

# find opencv package
find_package(OpenCV REQUIRED)

# all compile define
add_compile_definitions(TEST_DATA="${PROJECT_SOURCE_DIR}/test/data/")

# include directories
include_directories(class)
include_directories(template)

# add subdirectory and build
add_subdirectory(class)
add_subdirectory(template)
add_subdirectory(struct)
add_subdirectory(test)
# add_subdirectory(linked_list)
add_subdirectory(kmp)
add_subdirectory(leetcode)
# add_subdirectory(interview)