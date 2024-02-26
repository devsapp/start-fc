package example;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.Map;

import com.fasterxml.jackson.annotation.JsonProperty;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder(setterPrefix = "with")
public class HTTPTriggerResponse {
    private int statusCode;
    private Map<String, String> headers;

    @JsonProperty("isBase64Encoded")
    private boolean IsBase64Encoded;
    private String body;
}