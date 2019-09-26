provider "google" {
  project = "windy-collector-247209"
  region  = "europe-west4"
  zone    = "europe-west4-c"
}

resource "google_compute_instance" "vm_instance" {
  name         = "peisun-instance"
  machine_type = "n1-standard-1"

  tags = ["project", "visum_in_germany"]

  boot_disk {
    initialize_params {
      image = "gce-uefi-images/ubuntu-1804-lts"
    }
  }

  network_interface {
    network = "${google_compute_network.vpc_network.self_link}"
    access_config {
    }
  }
}

resource "google_compute_network" "vpc_network" {
  name                    = "peisun-network"
  auto_create_subnetworks = "true"
}

