/* register invoke and init handler.
*/
#include "http_handler.h"
#include "entrypoint.h"
using namespace Aliyun::FC::Handlers;
void SetInvokeAndInitHander()
{
    CustomRuntimeHandler::httpHandler = new HttpHandler();
    CustomRuntimeHandler::normalHandler = NULL;
}