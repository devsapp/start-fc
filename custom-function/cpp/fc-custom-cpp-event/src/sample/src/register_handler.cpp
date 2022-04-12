/* register invoke and init handler.
*/
#include "event_handler.h"
#include "entrypoint.h"
using namespace Aliyun::FC::Handlers;
void SetInvokeAndInitHander()
{
    CustomRuntimeHandler::normalHandler = new EventHandler();
    CustomRuntimeHandler::httpHandler = NULL;
}