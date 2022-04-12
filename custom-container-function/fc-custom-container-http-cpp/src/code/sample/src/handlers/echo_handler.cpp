#include "echo_handler.h"
using namespace std;
using namespace Pistache;

namespace Aliyun
{
    namespace FC
    {
        namespace Handlers
        {
            std::string EchoHttpHandler::mInitHandler;
            void EchoHttpHandler::OnInvoke(const FcContext &context, const Pistache::Http::Request &req,
                                           Pistache::Http::ResponseWriter &response)
            {
                if (req.method() == Http::Method::Post)
                {
                    response.send(Http::Code::Ok, + "Hello CPP, method = POST; Body = " + req.body(), MIME(Text, Plain));
                }

                else if (req.method() == Http::Method::Get)
                {
                    response.send(Http::Code::Ok, + "Hello CPP, method = GET", MIME(Text, Plain));
                }
            }

            void EchoHttpHandler::OnInitialize(const FcContext &context)
            {
                EchoHttpHandler::mInitHandler = context.initializer;
            }
        }
    }
}
