import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class MedicalRecordsSystem:
    def __init__(self):
        self.appointments = []
        self.patients = {}

    def schedule_appointment(self, patient_id, appointment_time):
        appointment = {
            'patient_id': patient_id,
            'appointment_time': appointment_time
        }
        self.appointments.append(appointment)

    def add_patient(self, patient_id, name, dob, address):
        patient_details = {
            'name': name,
            'dob': dob,
            'address': address
        }
        self.patients[patient_id] = patient_details

    def get_appointments(self):
        return self.appointments

    def find_patient(self, patient_id):
        return self.patients.get(patient_id, None)

class MedicalAppointmentApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Medical Appointment Scheduler")

        self.records_system = MedicalRecordsSystem()

        self.frame_input = tk.Frame(master, padx=10, pady=10)
        self.frame_input.pack()

        self.label_patient_id = tk.Label(self.frame_input, text="Patient ID:")
        self.label_patient_id.grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.entry_patient_id = tk.Entry(self.frame_input)
        self.entry_patient_id.grid(row=0, column=1, padx=5, pady=5)

        self.label_appointment_time = tk.Label(self.frame_input, text="Appointment Time (YYYY-MM-DD HH:MM):")
        self.label_appointment_time.grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.entry_appointment_time = tk.Entry(self.frame_input)
        self.entry_appointment_time.grid(row=1, column=1, padx=5, pady=5)

        self.label_name = tk.Label(self.frame_input, text="Patient Name:")
        self.label_name.grid(row=2, column=0, sticky='w', padx=5, pady=5)
        self.entry_name = tk.Entry(self.frame_input)
        self.entry_name.grid(row=2, column=1, padx=5, pady=5)

        self.label_dob = tk.Label(self.frame_input, text="Date of Birth (YYYY-MM-DD):")
        self.label_dob.grid(row=3, column=0, sticky='w', padx=5, pady=5)
        self.entry_dob = tk.Entry(self.frame_input)
        self.entry_dob.grid(row=3, column=1, padx=5, pady=5)

        self.label_address = tk.Label(self.frame_input, text="Address:")
        self.label_address.grid(row=4, column=0, sticky='w', padx=5, pady=5)
        self.entry_address = tk.Entry(self.frame_input)
        self.entry_address.grid(row=4, column=1, padx=5, pady=5)

        self.button_schedule_appointment = tk.Button(self.frame_input, text="Schedule Appointment", command=self.schedule_appointment)
        self.button_schedule_appointment.grid(row=5, column=0, columnspan=2, pady=10)

        self.button_add_patient = tk.Button(self.frame_input, text="Add Patient", command=self.add_patient)
        self.button_add_patient.grid(row=6, column=0, columnspan=2, pady=10)

        self.frame_search = tk.Frame(master, padx=10, pady=10)
        self.frame_search.pack()

        self.label_search_patient = tk.Label(self.frame_search, text="Search Patient ID:")
        self.label_search_patient.grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.entry_search_patient = tk.Entry(self.frame_search)
        self.entry_search_patient.grid(row=0, column=1, padx=5, pady=5)

        self.button_search_patient = tk.Button(self.frame_search, text="Search Patient", command=self.search_patient)
        self.button_search_patient.grid(row=0, column=2, padx=5, pady=5)

        self.label_patient_info = tk.Label(self.frame_search, text="")
        self.label_patient_info.grid(row=1, column=0, columnspan=3)

    def schedule_appointment(self):
        patient_id = self.entry_patient_id.get()
        appointment_time_str = self.entry_appointment_time.get()

        try:
            appointment_time = datetime.strptime(appointment_time_str, '%Y-%m-%d %H:%M')
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD HH:MM")
            return

        self.records_system.schedule_appointment(patient_id, appointment_time)
        messagebox.showinfo("Success", "Appointment scheduled successfully.")

    def add_patient(self):
        patient_id = self.entry_patient_id.get()
        name = self.entry_name.get()
        dob_str = self.entry_dob.get()
        address = self.entry_address.get()

        try:
            dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD")
            return

        self.records_system.add_patient(patient_id, name, dob, address)
        messagebox.showinfo("Success", "Patient added successfully.")

    def search_patient(self):
        patient_id = self.entry_search_patient.get()
        patient_info = self.records_system.find_patient(patient_id)

        if patient_info:
            info_str = f"Name: {patient_info['name']}\n"
            info_str += f"Date of Birth: {patient_info['dob']}\n"
            info_str += f"Address: {patient_info['address']}"
            self.label_patient_info.config(text=info_str)
        else:
            messagebox.showerror("Error", "Patient not found.")

def main():
    root = tk.Tk()
    root.geometry("400x500")
    app = MedicalAppointmentApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
