using System;
using System.IO;
using System.Text;
using System.Threading.Tasks;
using Aliyun.Serverless.Core;
using Microsoft.Extensions.Logging;

namespace Example
{
    public class Hello
    {
        public async Task<Stream> StreamHandler(Stream input, IFcContext context)
        {
            string strtxt="hello world! 你好，世界！";
            byte[] bytetxt = Encoding.UTF8.GetBytes(strtxt);
            Console.WriteLine(strtxt);
            MemoryStream ms = new MemoryStream();
            await input.CopyToAsync(ms);
            ms.Write(bytetxt, 0, bytetxt.Length);
            return ms;
        }

        static void Main(string[] args){}
    }
}