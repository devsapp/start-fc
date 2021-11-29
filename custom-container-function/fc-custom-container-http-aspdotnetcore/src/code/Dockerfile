FROM mcr.microsoft.com/dotnet/aspnet:5.0 AS base
WORKDIR /app
EXPOSE 80

FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /src
COPY ["asp-net-core-project/fc-project/fc-project.csproj", "./"]
COPY asp-net-core-project/fc-project .

RUN dotnet restore "./fc-project.csproj"
RUN dotnet build "fc-project.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "fc-project.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "fc-project.dll"]