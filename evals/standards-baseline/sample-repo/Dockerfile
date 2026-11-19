FROM golang:1.23 AS build
WORKDIR /src
COPY . .
RUN go build -o /pingboard .
FROM gcr.io/distroless/base
COPY --from=build /pingboard /pingboard
ENTRYPOINT ["/pingboard"]
