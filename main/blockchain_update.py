from operations import Blockchain,hospital_data,FederatedModelData
from hospital_1 import m_coeff_1,m_inter_1
from hospital_2 import m_coeff_2,m_inter_2
from hospital_3 import m_coeff_3,m_inter_3
hospital1 = hospital_data(hospital_name="apollo",hospital_id=1234,hospital_weight={'m_coeff' : m_coeff_1 ,'m_inter' : m_inter_1})
hospital2 = hospital_data(hospital_name="wilson",hospital_id=1235,hospital_weight={'m_coeff' : m_coeff_2 ,'m_inter' : m_inter_2})
hospital3 = hospital_data(hospital_name="AIIMS",hospital_id=1236,hospital_weight={'m_coeff' : m_coeff_3 ,'m_inter' : m_inter_3})
hospital_list = [hospital1.get_hospital_weight(),hospital2.get_hospital_weight()]
fed_avg = FederatedModelData(hospital_list)
blockchain = Blockchain(difficulty=3)
with open ("data.txt" , 'w') as f:
    while True :
        data = f"""data provided by hospital are {hospital_list}  , federated avg of all model are {fed_avg.get_avg()}"""
        blockchain.add_block(data=data)
        print(blockchain.get_last_block())
        f.write(str(blockchain.get_last_block()))




