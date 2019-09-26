provider "google" {
  project = "windy-collector-247209"
  region  = "europe-west4"
  zone    = "europe-west4-c"
}

# vm instance
resource "google_compute_instance" "vm_instance" {
  name         = "peisun-instance"
  machine_type = "n1-standard-1"

  tags = ["project", "visum-in-germany"]

  boot_disk {
    initialize_params {
      image = "gce-uefi-images/ubuntu-1804-lts"
      size  = "10"
    }
  }

  metadata = {
    ssh-keys = "peisun:${file("~/.ssh/peisun_rsa.pub")}"
  }

  network_interface {
    network = "${google_compute_network.vpc_network.self_link}"
    access_config {
    }
  }
}

# vpc network
resource "google_compute_network" "vpc_network" {
  name                    = "peisun-network"
  auto_create_subnetworks = "true"
}

resource "google_compute_firewall" "allow_ssh" {
  name          = "vm-allow-ssh"
  network       = "${google_compute_network.vpc_network.name}"
  direction     = "INGRESS"
  source_ranges = ["84.143.148.143/32"]

  allow {
    protocol = "tcp"
    ports    = ["22"]
  }
}
