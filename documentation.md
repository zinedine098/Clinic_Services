# 🏥 Dokumentasi Sistem Klinik

## Django Fullstack + Tailwind CSS (Best Practice Industri)

Dokumentasi ini menjelaskan **rencana pembangunan aplikasi klinik** menggunakan **Django Fullstack (tanpa API)**, **Django Template Engine**, dan **Tailwind CSS** dengan pendekatan **clean architecture, scalable, dan standar industri**.

---

## 🎯 Tujuan Sistem

Membangun aplikasi internal klinik untuk:

* Mengelola alur pasien secara end‑to‑end
* Mendukung proses medis nyata
* Aman (role-based access)
* Modern UI, cepat, dan maintainable

> Target: **aplikasi internal (intranet clinic system)**

---

## 🧠 Prinsip Arsitektur (Best Practice)

* ✅ Django ORM (tanpa raw SQL)
* ✅ Separation of Concerns (App per domain)
* ✅ Django Auth + Groups + Permissions
* ✅ Class Based Views (CBV)
* ✅ Reusable template components
* ✅ Service layer untuk logic kompleks
* ❌ Tanpa API / SPA / AJAX berat

---

## 👥 Role Pengguna

| Role    | Tanggung Jawab                |
| ------- | ----------------------------- |
| ADMIN   | Master data & user management |
| LOKET   | Registrasi pasien             |
| UGD     | Triage & penentuan poli       |
| DOKTER  | Pemeriksaan & resep           |
| FARMASI | Penyerahan obat               |

---

## 🗂️ Struktur App Django

```
clinic/
├─ accounts/        # Custom user, roles
├─ patients/        # Data pasien
├─ registrations/   # Pendaftaran & antrian
├─ triage/          # Proses UGD
├─ polyclinics/     # Poli
├─ doctors/         # Dokter
├─ examinations/    # Pemeriksaan
├─ pharmacy/        # Obat & resep
├─ templates/
│  ├─ base/
│  ├─ components/
│  ├─ auth/
│  ├─ dashboard/
│  ├─ registrations/
│  ├─ triage/
│  ├─ examinations/
│  └─ pharmacy/
└─ static/
   ├─ css/
   └─ js/
```

---

## 🎨 Frontend Stack (Modern & Industry‑Ready)

### CSS & UI

* **Tailwind CSS** → utility-first
* **django-tailwind** → integrasi resmi
* **@tailwind/forms** → form clean
* **@tailwind/typography** → konten medis

### UI / UX

* **Alpine.js** → interaksi ringan
* **Heroicons** → icon modern
* **Headless UI (optional)** → dropdown, modal

> ❌ Tidak menggunakan Bootstrap / jQuery

---

## 🔐 Authentication & Authorization

### Authentication

* Django built‑in auth
* Login berbasis session

### Authorization

* Django Groups:

  * admin
  * loket
  * ugd
  * dokter
  * farmasi

* Implementasi:

  * `LoginRequiredMixin`
  * `UserPassesTestMixin`
  * Custom permission decorator

---

## 🧱 Desain Database (ORM Django)

### User (Custom)

```py
class User(AbstractUser):
    pass
```

---

### Patient

```py
class Patient(models.Model):
    medical_record_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    phone = models.CharField(max_length=20)
```

---

### Registration

```py
class Registration(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
```

---

### Polyclinic

```py
class Polyclinic(models.Model):
    name = models.CharField(max_length=100)
```

---

### Doctor

```py
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    polyclinic = models.ForeignKey(Polyclinic, on_delete=models.CASCADE)
```

---

### Triage

```py
class Triage(models.Model):
    registration = models.OneToOneField(Registration, on_delete=models.CASCADE)
    complaint = models.TextField()
    urgency_level = models.CharField(max_length=20)
    referred_polyclinic = models.ForeignKey(Polyclinic, on_delete=models.CASCADE)
```

---

### Examination

```py
class Examination(models.Model):
    registration = models.OneToOneField(Registration, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    notes = models.TextField()
```

---

### Medicine

```py
class Medicine(models.Model):
    name = models.CharField(max_length=100)
    stock = models.PositiveIntegerField()
```

---

### Prescription

```py
class Prescription(models.Model):
    examination = models.ForeignKey(Examination, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
```

---

## 🔄 Alur Sistem (Real Workflow)

1️⃣ **Loket**

* Input data pasien
* Buat registrasi

2️⃣ **UGD**

* Triage pasien
* Tentukan poli tujuan

3️⃣ **Dokter**

* Pemeriksaan pasien
* Input diagnosis & resep

4️⃣ **Farmasi**

* Terima resep
* Kurangi stok
* Serahkan obat

---

## 🧩 Pola View (Best Practice)

* List → `ListView`
* Create → `CreateView`
* Update → `UpdateView`
* Detail → `DetailView`

Logic kompleks → **Service Layer**

---

## 🏭 Library & Tools Tambahan

| Library             | Fungsi                |
| ------------------- | --------------------- |
| django-environ      | env config            |
| django-crispy-forms | optional form control |
| django-filter       | filtering data        |
| whitenoise          | static production     |
| python-decouple     | env separation        |

---

## 🚀 Tahapan Pembangunan

1. Setup project & Tailwind
2. Custom user & groups
3. Master data (Poli, Obat)
4. Flow pasien
5. UI dashboard per role
6. Hardening permission
7. Testing & deployment

---

## 🎓 Nilai Plus (Industri & Portfolio)

* Arsitektur jelas
* UI modern
* Role‑based
* Tidak over‑engineering
* Mudah dikembangkan

---

📌 **Next step yang bisa kita lanjutkan:**

* Layout dashboard Tailwind
* Permission mixin per role
* Contoh 1 app full (models + views + template)
* Checklist production deployment

Tinggal bilang mau lanjut ke bagian mana 👌
