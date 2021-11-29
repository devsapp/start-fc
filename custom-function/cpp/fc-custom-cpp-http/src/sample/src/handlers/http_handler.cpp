#include "http_handler.h"
using namespace std;
using namespace Pistache;

namespace Aliyun
{
    namespace FC
    {
        namespace Handlers
        {
            std::string HttpHandler::mInitHandler;
            void HttpHandler::OnInvoke(const FcContext &context, const Pistache::Http::Request &req,
                                       Pistache::Http::ResponseWriter &response)
            {
                response.send(Http::Code::Ok, req.body());
            }

            void HttpHandler::OnInitialize(const FcContext &context)
            {
                HttpHandler::mInitHandler = context.initializer;
            }
        }
    }
}