FROM mcr.microsoft.com/dotnet/sdk:6.0 AS base

WORKDIR /src
COPY ./dotnet6-web-demo .

RUN dotnet restore
RUN dotnet build -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=base /app .
ENTRYPOINT ["dotnet", "dotnet6-web-demo.dll"]