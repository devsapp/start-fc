FROM maven:3.8.2-openjdk-8

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY src ./src
COPY pom.xml ./pom.xml
COPY settings.xml /usr/share/maven/conf/settings.xml
RUN mvn package

## prod image on FC
FROM maven:3.8.2-openjdk-8
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY --from=0 /usr/src/app/target/demo-0.1.0.jar  /usr/src/app/demo.jar
ENTRYPOINT ["java", "-jar", "demo.jar"]