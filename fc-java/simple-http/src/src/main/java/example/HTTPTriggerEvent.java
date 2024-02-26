package example;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.util.Map;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder(setterPrefix = "with")
public class HTTPTriggerEvent {
    private String version;
    private String rawPath;
    private Map<String, String> headers;
    private Map<String, String> queryParameters;
    private RequestContext requestContext;

    @JsonProperty("isBase64Encoded")
    private boolean IsBase64Encoded;
    private String body;

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder(setterPrefix = "with")
    public static class RequestContext {
        private String accountId;
        private String domainName;
        private String domainPrefix;
        private HttpInfo http;
        private String requestId;
        private String time;
        private String timeEpoch;

        @Data
        @NoArgsConstructor
        @AllArgsConstructor
        @Builder(setterPrefix = "with")
        public static class HttpInfo {
            private String method;
            private String path;
            private String protocol;
            private String sourceIp;
            private String userAgent;
        }
    }

}
