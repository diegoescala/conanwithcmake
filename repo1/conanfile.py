from conan import ConanFile
from conan.tools.cmake import CMake

class Repo1Recipe(ConanFile):
    name = "repo1"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def layout(self):
        #set build folder
        self.folders.build = "build"
        self.folders.source = "."
        self.folders.generators = "build"
