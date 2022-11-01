cmake_minimum_required(VERSION VERSION 2.6)
project(interview)

file(GLOB_RECURSE SRC_LIST "${CMAKE_CURRENT_LIST_DIR}/*.cpp")
file(GLOB_RECURSE HEAD_LIST "${CMAKE_CURRENT_LIST_DIR}/*.hpp")

add_library(interview ${SRC_LIST} ${HEAD_LIST})
