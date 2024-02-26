using System;
using System.Collections.Generic;
using System.Text;
using System.Text.Json;
using Aliyun.Serverless.Core;
using Microsoft.Extensions.Logging;

namespace Example
{
    public class Hello
    {
        public class HTTPTriggerEvent
        {
            public string Version { get; set; }
            public string RawPath { get; set; }
            public string Body { get; set; }
            public bool IsBase64Encoded { get; set; }
            public RequestContext RequestContext { get; set; }
            public Dictionary<string, string> Headers { get; set; }
            public Dictionary<string, string> QueryParameters { get; set; }

            public override string ToString()
            {
                return JsonSerializer.Serialize(this);
            }
        }

        public class RequestContext
        {
            public string AccountId { get; set; }
            public string DomainName { get; set; }
            public string DomainPrefix { get; set; }
            public string RequestId { get; set; }
            public string Time { get; set; }
            public string TimeEpoch { get; set; }
            public Dictionary<string, string> Http { get; set; }
        }

        public class HTTPTriggerResponse
        {
            public int StatusCode { get; set; }
            public Dictionary<string, string> Headers { get; set; }
            public bool IsBase64Encoded { get; set; }
            public string Body { get; set; }
        }

        public HTTPTriggerResponse PocoHandler(HTTPTriggerEvent input, IFcContext context)
        {
            context.Logger.LogInformation("receive event: {0}", input.ToString());
            string requestBody = input.Body;
            if (input.IsBase64Encoded)
            {
                byte[] decodedBytes = Convert.FromBase64String(input.Body);
                requestBody = Encoding.UTF8.GetString(decodedBytes);
            }
            return new HTTPTriggerResponse
            {
                StatusCode = 200,
                IsBase64Encoded = false,
                Body = requestBody
            };
        }
        static void Main(string[] args){}
    }
}