var builder = WebApplication.CreateBuilder(args);
builder.WebHost.UseUrls("http://0.0.0.0:9000"); //修改默认端口,必须监听0.0.0.0
var app = builder.Build();

app.MapGet("/", () => "Hello World!\n");

// 添加请求路径 /test
app.MapGet("/test", () => {
    // 可在此处添加代码
    return "this is a test function.\n";
});

app.Run();