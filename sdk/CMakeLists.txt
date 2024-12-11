cmake_minimum_required(VERSION 3.15)
# Add this line to include Conan-generated cmake files
include(${CMAKE_BINARY_DIR}/conan_toolchain.cmake)

project(sdk)

# no boost, build static library
set(CMAKE_CXX_STANDARD 17)

find_package(repo1 CONFIG REQUIRED)  # Add this line before using repo1

# Debug library info
get_target_property(REPO1_LIBS repo1::repo1 INTERFACE_LINK_LIBRARIES)
message("repo1 link libraries: ${REPO1_LIBS}")

get_target_property(REPO1_LOCATION repo1::repo1 LOCATION)
message("repo1 library location: ${REPO1_LOCATION}")

# Build the executable and link it
add_executable(sdk src/main.cpp)
target_link_libraries(sdk PRIVATE repo1::repo1)

# Debug executable link info
get_target_property(SDK_LIBS sdk LINK_LIBRARIES)
message("sdk link libraries: ${SDK_LIBS}")

# More debug info
get_target_property(SDK_INCLUDE_DIRS sdk INCLUDE_DIRECTORIES)
message("sdk include dirs: ${SDK_INCLUDE_DIRS}")

# Make sure the include directories are available
target_include_directories(sdk PRIVATE include)
