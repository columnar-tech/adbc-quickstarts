plugins {
    kotlin("jvm") version "2.3.21"
    application
}

repositories {
    mavenCentral()
}

val arrowVersion = "18.3.0"
val adbcVersion = "0.21.0"

dependencies {
    implementation("org.apache.arrow:arrow-memory-core:$arrowVersion")
    implementation("org.apache.arrow:arrow-memory-netty:$arrowVersion")
    implementation("org.apache.arrow:arrow-vector:$arrowVersion")
    implementation("org.apache.arrow.adbc:adbc-core:$adbcVersion")
    implementation("org.apache.arrow.adbc:adbc-driver-manager:$adbcVersion")
    implementation("org.apache.arrow.adbc:adbc-driver-jni:$adbcVersion")
    implementation("org.slf4j:slf4j-nop:2.0.16")
}

application {
    mainClass.set("MainKt")
    applicationDefaultJvmArgs =
        listOf(
            "--add-opens=java.base/java.nio=ALL-UNNAMED",
            "--enable-native-access=ALL-UNNAMED",
            "--sun-misc-unsafe-memory-access=allow",
        )
}
