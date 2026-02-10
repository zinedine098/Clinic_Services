from django.core.management.base import BaseCommand
from clinic_auth.models import User
from polyclinics.models import Polyclinic
from pharmacy.models import Medicine


class Command(BaseCommand):
    help = "Setup initial data for clinic"

    def handle(self, *args, **kwargs):
        # Create Superuser
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                "admin", "admin@example.com", "admin123", role="admin"
            )
            self.stdout.write(
                self.style.SUCCESS('Superuser "admin" created (pass: admin123)')
            )

        # Create Polyclinics
        polis = [
            "Poli Umum",
            "Poli Gigi",
            "Poli Anak",
            "Poli Kandungan",
            "Poli Penyakit Dalam",
        ]
        for name in polis:
            Polyclinic.objects.get_or_create(
                name=name,
                defaults={"description": f"Pelayanan {name.lower()} profesional"},
            )
        self.stdout.write(self.style.SUCCESS(f"{len(polis)} Polyclinics created"))

        # Create Medicines
        meds = [
            ("Paracetamol 500mg", 100, "tablet", 5000),
            ("Amoxicillin 500mg", 50, "kapsul", 15000),
            ("Vitamin C", 200, "tablet", 2000),
            ("OBH Sirup", 30, "botol", 25000),
            ("Antasida Doen", 100, "tablet", 3000),
        ]
        for name, stock, unit, price in meds:
            Medicine.objects.get_or_create(
                name=name, defaults={"stock": stock, "unit": unit, "price": price}
            )
        self.stdout.write(self.style.SUCCESS(f"{len(meds)} Medicines created"))
