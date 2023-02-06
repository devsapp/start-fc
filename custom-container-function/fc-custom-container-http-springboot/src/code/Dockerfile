FROM rsonghuster/openjdk8:stretch

RUN mkdir -p /usr/app
WORKDIR /usr/app
COPY src ./src
COPY pom.xml ./pom.xml
COPY settings.xml /usr/share/maven/conf/settings.xml
RUN mvn package
ENTRYPOINT ["java", "-jar", "/usr/app/target/demo-0.1.0.jar"]