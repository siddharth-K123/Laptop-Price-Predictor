import pickle
import json
import config
import numpy as np

class LaptopPrice():

    def __init__(self, user_data) :
        self.model_file_path = 'model.pkl'
        self.user_data = user_data
        

    def load_saved_data(self):
        with open(self.model_file_path,'rb') as f:
            self.model = pickle.load(f)

        with open('project_data.json','r') as f:
            self.project_data = json.load(f)
        

        

    def get_predicted_price(self):

        self.load_saved_data()

        Company = self.user_data['Company']
        # Company = 'Company_' + Company
        #print(Company)
        TypeName  = self.user_data['TypeName']
        #print(TypeName)
        Gpu_Brand  = self.user_data['Gpu_Brand']
        os  = self.user_data['os']
        Cpu_Brand  = self.user_data['Cpu_Brand']

        #print("hi")

        # Company  = self.project_data['Company'][Company]
        # TypeName  = self.project_data['TypeName'][TypeName]
        # Gpu_Brand  = self.project_data['Gpu_Brand'][Gpu_Brand]
        # os  = self.project_data['os'][os]
        # Cpu_Brand  = self.project_data['Cpu_Brand'][Cpu_Brand]

        Company = 'Company_' + Company
        Company_index = np.where(np.array(self.project_data['columns']) == Company)[0][0]
        #print(Company_index)

        TypeName = 'TypeName_' + TypeName
        TypeName_index = np.where(np.array(self.project_data['columns']) == TypeName)[0][0]

        Gpu_Brand = 'Gpu Brand_' + Gpu_Brand
        Gpu_Brand_index = np.where(np.array(self.project_data['columns']) == Gpu_Brand)[0][0]

        os = 'os_' + os
        os_index = np.where(np.array(self.project_data['columns']) == os)[0][0]
        
        
        Cpu_Brand = 'Cpu Brand_' + Cpu_Brand
        Cpu_Brand_index = np.where(np.array(self.project_data['columns']) == Cpu_Brand)[0][0]

        
        print('Company_index :',Company_index)
        print('Gpu_Brand_index :',Gpu_Brand_index)

        col_count = len(self.project_data['columns'])
        #print(col_count)
        test_array = np.zeros(col_count)
        print("test array : ",test_array)
        test_array[0] = eval(self.user_data['Ram'])
        #print(test_array[0])
        test_array[1] = eval(self.user_data['Weight'])
        test_array[2] = eval(self.user_data['TouchScreen'])
        test_array[3] = eval(self.user_data['Ips'])
        test_array[4] = eval(self.user_data['PPI'])
        test_array[5] = eval(self.user_data['HDD'])
        test_array[6] = eval(self.user_data['SSD'])
        test_array[Company_index] = 1
        test_array[TypeName_index] = 1
        test_array[Gpu_Brand_index] = 1
        test_array[os_index] = 1
        test_array[Cpu_Brand_index] = 1

        
        
        print(test_array)



        predicted_charges = np.around(self.model.predict([test_array])[0],3)
        print('predicted_charges :',predicted_charges)
        return predicted_charges

if __name__ == "__main__":
    lap = LaptopPrice()
    lap