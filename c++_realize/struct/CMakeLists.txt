cmake_minimum_required(VERSION VERSION 2.6)
project(struct)


# message("cmake message: ${SRC_LIST}" )

file(GLOB_RECURSE SRC_LIST "${CMAKE_CURRENT_LIST_DIR}/*.cpp")

add_library(struct ${SRC_LIST})