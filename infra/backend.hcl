# infra/backend.hcl
bucket       = "tfstate-calculadora-mateomunozb"
key          = "calculadora/terraform.tfstate"
region       = "us-east-1"
use_lockfile = true