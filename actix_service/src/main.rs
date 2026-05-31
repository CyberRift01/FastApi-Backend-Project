use actix_web::{get,APP,HttpServer, Responder};

#[get("/health")]
async fn health()->impl Responder{
    "Rust service running"
}

#[actix_web::main]
async fn main()-> std::io::Result<()> {
    HttpServer::new(||APP::new().service(health))
        .bind(("0.0.0.0", /8081))?
        .run()
        .await()
}