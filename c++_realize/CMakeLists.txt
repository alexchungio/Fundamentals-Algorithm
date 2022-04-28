cmake_minimum_required(VERSION VERSION 2.6)
project(cplusplus_experiment)

# include directories
include_directories(class)

# add subdirectory and build
add_subdirectory(class)
add_subdirectory(test)
add_subdirectory(template)
add_subdirectory(struct)