# Etap bazowy dla runtime
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base
WORKDIR /app
EXPOSE 8080

# Etap budowania z SDK
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY ["FlatSwap.csproj", "./"]
RUN dotnet restore "./FlatSwap.csproj"
COPY . .
RUN dotnet build "./FlatSwap.csproj" -c Release -o /app/build

# Etap publikacji
FROM build AS publish
RUN dotnet publish "./FlatSwap.csproj" -c Release -o /app/publish

# Etap koñcowy
FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "FlatSwap.dll"]
