#include <mutex>
#include <deque>
#include <memory>
#include <cmath>
#include <thread>
#include <queue>
#include <iostream>

// C and C++ mix programming
// tell compiler to treat the enclose code as C language code. not C++ code.
// ensure the function can be linked with C language code or liabrary 
#ifdef __cplusplus
extern "C"{
#endif

typedef struct TimeStamp_ {
    uint32_t sec;
    uint32_t nsec;
} TimeStamp;

typedef struct DataHeader_ {
    TimeStamp stamp;
    uint32_t seq;
    int8_t frameId[32];
} DataHeader;

typedef struct Point3Fwithcovariance_ {
    float x;
    float y;
    float z;
    float covariance[9];
} Point3FWithcovariance;

typedef struct quaternion4Fwithcovariance_ {
    float x;
    float y;
    float z;
    float w;
    float covariance[9];
} Quaternion4Fwithcovariance;

typedef struct Pose_ {
    Point3FWithcovariance position;
    Quaternion4Fwithcovariance orientation;
} Pose;

typedef struct Velocity_ {
Point3FWithcovariance linear;
Point3FWithcovariance angular;
} Velocity;

typedef struct Acceleration_ {
    Point3FWithcovariance angular;
    Point3FWithcovariance linear;
} Acceleration;


typedef struct LocationData_ {
    DataHeader header;
    Pose pose;
    Velocity velocity;
    Acceleration acceleration;
    float odometry;
    uint8_t utmLongitudeZone;
    uint8_t locatioState;
    uint8_t type;
    uint8_t resetCount;
    int8_t utmLatitudezone;
} LocationData;

typedef struct LocationPerception_ {
    LocationData location;
    bool isLocationUpdate;
} LocationPerception;

#ifdef __cplusplus
}
#endif


std::mutex m_mutexLocation;
std::deque<LocationPerception> location_queue;

// lambda funtion
// [capture](parameter_list) -> return_type { function_body }
auto queue_producer = []() {
    while (true) {
        {
            std::lock_guard<std::mutex> guard(m_mutexLocation);
            LocationPerception location_data;
            while(location_queue.size() > 100) {
                location_queue.pop_front();
            }   
            location_queue.push_back(location_data);
            location_queue.back().isLocationUpdate = true; // inside loack region
        }   
        // location_queue.back().isLocationUpdate = true;  // outside lock region, which is unsafe. may lead coredump.
        std::cout << "running producer" << std::endl;
    }
    
};

auto queue_consumer = [](int id) {

     while (true) {
        {
            std::lock_guard<std::mutex> guard(m_mutexLocation);
            std::deque<LocationPerception> location_queue_copy;
            location_queue_copy.resize(100);
            
            static int index = 0;
            if(index == 50){
                location_queue.clear();
                index = 0;
            }
            location_queue_copy.assign(location_queue.begin(), location_queue.end());
            ++index;  
        }   
        std::cout << "running consumer id " << id << std::endl;
    }
    

};


int main() {
    
    std::thread t1(queue_producer);
    std::thread t2(queue_consumer, 1);
    std::thread t3(queue_consumer, 2);
    
    t1.join();
    t2.join();
    t3.join();

    return 0;
}