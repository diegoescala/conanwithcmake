from conan import ConanFile
from conan.tools.cmake import CMake

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
