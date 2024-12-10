cmake_minimum_required(VERSION 3.22)
project(repo1)

# no boost, build static library
set(CMAKE_CXX_STANDARD 17)
add_library(repo1 STATIC src/repo1.cpp)
