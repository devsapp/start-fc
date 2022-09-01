using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

namespace dotnetcore2webapi.Controllers
{
    public class ValuesController : ControllerBase
    {
        // POST /initialize
        [Route("initialize")]
        [HttpPost]
        public void Initialize()
        {
            Console.WriteLine("Hello initialize!");
        }

        // GET api/values
        [Route("api/values")]
        [HttpGet]
        public ActionResult<IEnumerable<string>> HandleRequest()
        {
            return new string[] { "value1", "value2" };
        }

    }
}
