from conan import ConanFile
from conan.tools.cmake import CMake
from conan.tools.files import copy

class Repo1Recipe(ConanFile):
    name = "repo1"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"
    options = {"arch": ["armv8", "x86"]}
    default_options = {"arch": "armv8"}
    platform = "armv8"
    
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def layout(self):
        self.folders.build = "build"
        self.folders.generators = "build"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        # Copy headers from source include dir to package include dir
        copy(self, "*.h", dst=f"{self.package_folder}/include", src="include")
        # Copy libs from build directory
        copy(self, "*.a", src="build", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["repo1"]  # Name of your library
        self.cpp_info.includedirs = ["include"]  # Specify include directory
