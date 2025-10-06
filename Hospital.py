class Haospital:
    def __init__(self):
        self.doctors = []
        self.patient = []
        self.appointment = []
    
    def add_docters(self,doctor_name,doctor_age,doctor_specilist_in):
        if doctor_name not in self.doctors:
            doct = {'Doctor_name':doctor_name,'Doctor_age':doctor_age,'Doctor_speclist':doctor_specilist_in}
            self.doctors.append(doct)
            print('Doctor is Added suessfully...')
        else:
            print('Doctor is already existed')
        
    def view_doctors(self):
        for details in self.doctors:
            print(f"Doctor_Name: {details['Doctor_name']}, Doctor_Age: {details['Doctor_age']}, Doctor_specilist: {details['Doctor_speclist']}")
    
    def add_patient(self,Patient_name,age,disease):
        if Patient_name not in self.patient:
            pat = {"Patient_name":Patient_name,'Age':age,'Disease':disease}
            self.patient.append(pat)
            print('Patient reocrd is added suessfully!!')
        else:
            print('Patient already Exits')
    
    def view_patient(self):
        for n in self.patient:
            print(f"Patient_Name: {n['Patient_name']}, Patient_Age: {n['Age']}, Patient_Disease: {n['Disease']}")
        
    def book_appointment(self,patient_name,doctor_name,date):
        doctor = next((d for d in self.doctors if d["Doctor_name"] == doctor_name),None)
        patient = next((p for p in self.patient if p["Patient_name"] == patient_name),None)

        if doctor and patient:
            appt = {"Patient":patient_name,"Doctor":doctor_name,"Date":date}
            self.appointment.append(appt)
            print('Appointment booked suessfully...')
        else:
            print('Doctor or Patient not found....')
    
    def view_appointment(self):
        for a in self.patient:
            print(f"Patient: {a['Patient']}, Doctor: {a['Doctor']}, Date: {a['Date']}")
    
    def search_doctor_by_speacilist(self,specilist):
        result = [s for s in self.doctors if self.doctors["Doctor_speclist"] == specilist]
        if result:
            for d in result:
                print(f"Doctor: {d['Doctor_Name']}, Doctor_specilist: {d['Doctor_specilist']}")
        else:
            print('No doctor found with that specilaty')
    
    def update_patient_disease(self,name,new_disease):
        for p in self.patient:
            if p["Patient_name"] == name:
                p["Patient_Disease"] == new_disease
                print('Patient disease updated.')
                return
        print('Patient not found')
    
    def generater_billing(self,patient_name,consultation_fee,medicine_fee):
        total = consultation_fee + medicine_fee
        print(f"Bill for {patient_name}: {total} INR")
    
H = Haospital()

def menu():
    print('\n--------Welcome to Hospital Management System--------')
    print('1. Add Doctors')
    print('2. View Doctors')
    print('3. Add Patients')
    print('4. View Patient')
    print('5. Book_Appointent')
    print('6. View Appointment')
    print('7. Search_Doctor_By_Speacilist')
    print('8. Update_Patient_Disease')
    print('9. Generator Billing')
    print('10. Exit')

while True:
    menu()

    choice = int(input('Enter your choice(1-10): '))

    if choice == 1:
        doct_name = input('Enter your name: ')
        doct_Age = int(input('Enter your Age: '))
        doct_specilist = input('Enter your Specilist: ')
        H.add_docters(doct_name,doct_Age,doct_specilist)
    
    elif choice == 2:
        H.view_doctors()
    
    elif choice == 3:
        pati_name = input('Enter your name: ')
        pati_Age = int(input('Enter your age: '))
        Deiease = input('Enter your Diease: ')
        H.add_patient(pati_name,pati_Age,Deiease)
    
    elif choice == 4:
        H.view_patient()
    
    elif choice == 5:
        patient_name = input('Enter your patient_name: ')
        Doct_name = input('Enter your Docter_name: ')
        date = input('Enter the date like this: [##/##/####]')
        H.book_appointment(patient_name,Doct_name,Deiease)
    
    elif choice == 6:
        H.view_appointment()
    
    elif choice == 7:
        Specilist = input('Enter your Specilist: ')
        H.search_doctor_by_speacilist(Specilist)
    
    elif choice == 8:
        patient_name = input('Enter your name: ')
        Diease = input('Enter your speacial diease: ')
        H.update_patient_disease(patient_name,Diease)
    
    elif choice == 9:
        pati_name = input('Enter your Name: ')
        Consul = int(input('Enter the consulation_fees: '))
        medicine = int(input('Enter your medical diease medicine: '))
        H.generater_billing(pati_name,Consul,medicine)
    
    elif choice == 10:
        print('Thank you Sir Visit Again sir')
        break

    else:
        print('Invaild choice sir')