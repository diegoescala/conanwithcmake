#include <repo1/repo1.h>
// This will show the full path of repo1.h during compilation
// #include "include/repo1.h"
#include <iostream>

int main() {
    Repo1 repo1;
    repo1.repo1();

    std::cout << "Hello, SDK!" << std::endl;
}
