# CodeDNA Final Validation

Fresh immutable provider-evidence fixture for CodeDNA zero-touch onboarding validation.

- order-api intentionally includes urllib3 1.26.5
- inventory-api does not include urllib3 directly
- CI publishes one CycloneDX SBOM per service
- deployment workflow creates GitHub deployment evidence
