from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout

class SdkRecipe(ConanFile):
    name = "sdk"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    # dependencies:
    # repo1
    requires = "repo1/0.1"
    
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def layout(self):
        self.folders.build = "build"
        self.folders.generators = "build"
