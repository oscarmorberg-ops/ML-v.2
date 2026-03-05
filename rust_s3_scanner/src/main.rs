use lambda_runtime::{handler_fn, Context, Error};
use serde_json::Value;

#[tokio::main]
async fn main() -> Result<(), Error> {
    lambda_runtime::run(handler_fn(deep_hell_handler)).await
}

async fn deep_hell_handler(event: Value, _ctx: Context) -> Result<Value, Error> {
    Ok(serde_json::json!({"status": "Deep Hell Rust S3 scanner LIVE!"}))
}
