/* register invoke and init handler.
*/
#include "echo_handler.h"
#include "entrypoint.h"
using namespace Aliyun::FC::Handlers;
void SetInvokeAndInitHander()
{
    CustomRuntimeHandler::normalHandler = NULL;
    CustomRuntimeHandler::httpHandler = new EchoHttpHandler();
}