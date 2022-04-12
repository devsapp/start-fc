namespace FSharpDemo.Controllers

open System
open System.Collections.Generic
open System.Linq
open System.Threading.Tasks
open Microsoft.AspNetCore.Mvc
open Microsoft.Extensions.Logging
open FSharpDemo

[<ApiController>]
[<Route("/")>]
type HomeController (logger : ILogger<HomeController>) =
    inherit ControllerBase()
    
    [<HttpGet>]
    member this.Get() =
       let values = [|"hello"; "world"|]
       ActionResult<string[]>(values)
