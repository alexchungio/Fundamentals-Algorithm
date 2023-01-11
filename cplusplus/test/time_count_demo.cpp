#include <iostream>
#include <chrono>
#include <thread>

int main()
{
    std::chrono::time_point<std::chrono::steady_clock> start = std::chrono::steady_clock::now();
    // auto start = std::chrono::steady_clock::now();
    
    std::this_thread::sleep_for(std::chrono::seconds(2));
    
    auto end = std::chrono::steady_clock::now();
    
    std::chrono::duration<double> elapsed = end - start;
    
    std::cout << elapsed.count() << std::endl;

    return 0;
}