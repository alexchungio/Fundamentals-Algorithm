cmake_minimum_required(VERSION VERSION 3.0)
project(class)

set(SRC_LIST stock.cpp)
set(HEAD_LIST stock.hpp)

message("cmake message: ${SRC_LIST}" )

add_library(class ${SRC_LIST} ${HEAD_LSIT})