#include "event_handler.h"
using namespace std;
using namespace Pistache;

namespace Aliyun
{
    namespace FC
    {
        namespace Handlers
        {
            std::string EventHandler::mInitHandler;
            void EventHandler::OnInvoke(const string &payload, const FcContext &context, string &response)
            {
                response = payload;
            }

            void EventHandler::OnInitialize(const FcContext &context)
            {
                EventHandler::mInitHandler = context.initializer;
            }
        }
    }
}