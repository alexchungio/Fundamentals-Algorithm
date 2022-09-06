cmake_minimum_required(VERSION VERSION 2.6)
project(cplusplus_experiment)

# set cmaker standard
set(CMAKE_CXX_STANDARD 11)

# include directories
include_directories(class)
include_directories(template)

# add subdirectory and build
add_subdirectory(class)
add_subdirectory(template)
add_subdirectory(struct)
add_subdirectory(test)