#include "echo_handler.h"
#include<opencv2/opencv.hpp>
using namespace std;
using namespace Pistache;
using namespace cv;

namespace Aliyun
{
    namespace FC
    {
        namespace Handlers
        {
            std::string EchoHandler::mInitHandler;
            void EchoHandler::OnInvoke(const string &payload, const FcContext &context, string &response)
            {
                Mat src = imread("/usr/src/app/dog.jpg");
                cout << "Width : " << src.cols << endl;
                cout << "Height: " << src.rows << endl; 
                response = EchoHandler::mInitHandler + payload;
            }

            void EchoHandler::OnInitialize(const FcContext &context)
            {
                EchoHandler::mInitHandler = context.initializer;
            }

            std::string EchoHttpHandler::mInitHandler;
            void EchoHttpHandler::OnInvoke(const FcContext &context, const Pistache::Http::Request &req,
                                           Pistache::Http::ResponseWriter &response)
            {
                // HTTP Function, do your things
                response.send(Http::Code::Ok, EchoHttpHandler::mInitHandler + req.body());
            }

            void EchoHttpHandler::OnInitialize(const FcContext &context)
            {
                // HTTP Function Initialize, do your things
                EchoHttpHandler::mInitHandler = context.initializer;
            }
        }
    }
}
