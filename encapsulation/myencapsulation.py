class Health:

    def __init__(self, patient, disease):
        self.__patient = patient          # private
        self.__diseases = [disease]       # private 

    def add_disease(self, disease):
        if disease:
            self.__diseases.append(disease)

    def get_patient(self):
        return self.__patient

    def get_diseases(self):
        return self.__diseases.copy()   

    def get_information(self):
        return f"{self.__patient}, {', '.join(self.__diseases)}"


# Test
acc = Health("Alex", "Common Cold")
acc.add_disease("Covid-19")

print(acc.get_information())
# Output: Alex, Common Cold, Covid-19

# print(acc.__patient)   ERROR (private!)