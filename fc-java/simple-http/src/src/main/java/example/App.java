package example;

import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;

import com.aliyun.fc.runtime.Context;
import com.aliyun.fc.runtime.PojoRequestHandler;

/**
 * HTTP Trigger demo
 *
 */
public class App implements PojoRequestHandler<HTTPTriggerEvent, HTTPTriggerResponse> {

    @Override
    public HTTPTriggerResponse handleRequest(HTTPTriggerEvent request, Context context) {
        context.getLogger().info("Receive HTTP Trigger request: " + request.toString());
        String requestBody = request.getBody();
        if (request.isIsBase64Encoded()) {
            requestBody = new String(java.util.Base64.getDecoder().decode(request.getBody()), StandardCharsets.UTF_8);
        }
        String message = "HTTP Trigger request body: " + requestBody;
        context.getLogger().info(message);
        Map<String, String> headers = new HashMap<>();
        headers.put("Content-Type", "text/plain");
        return HTTPTriggerResponse.builder().withStatusCode(200).withHeaders(headers).withBody(request.getBody())
                .withIsBase64Encoded(request.isIsBase64Encoded()).build();
    }
}
