cmake_minimum_required(VERSION 3.22)
project(repo1)

# no boost, build static library
set(CMAKE_CXX_STANDARD 17)

add_library(repo1 STATIC src/repo1.cpp)
add_library(repo1::repo1 ALIAS repo1)

target_include_directories(repo1 PUBLIC 
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>
)

include(GNUInstallDirs)
install(TARGETS repo1
    EXPORT repo1Targets
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

install(EXPORT repo1Targets
    FILE repo1Targets.cmake
    NAMESPACE repo1::
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/repo1
)

# Generate and install the config file
include(CMakePackageConfigHelpers)
configure_package_config_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
    ${CMAKE_CURRENT_BINARY_DIR}/repo1Config.cmake
    INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/repo1
)

install(FILES
    ${CMAKE_CURRENT_BINARY_DIR}/repo1Config.cmake
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/repo1
)

# Install headers
install(DIRECTORY include/
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)
