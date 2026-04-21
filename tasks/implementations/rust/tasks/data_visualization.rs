pub fn start(size: &str, port: u16, fixtures_root: &str) {
    crate::tasks::service_support::start_http_service("data_visualization", port);
}
