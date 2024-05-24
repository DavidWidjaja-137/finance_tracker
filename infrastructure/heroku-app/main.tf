

terraform {
  required_providers {
    heroku = {
      source = "heroku/heroku"
      version = "5.2.8"
    }
  }
}

# source Heroku api key from environmental variables
provider "heroku" {}

resource "heroku_app" "this" {
    name = "personal-finance-tracker"
    region = "us"
    acm = true
}

resource "heroku_build" "this" {
    app_id = heroku_app.this.id

    source {
        path = "app"
    }
}

resource "heroku_formation" "this" {
    app_id = heroku_app.this.id
    type = "web"
    quantity = 1
    size = "Basic"
}

resource "heroku_domain" "this" {
    app_id = heroku_app.this.id
    hostname = "prod.david-pw.com"
}