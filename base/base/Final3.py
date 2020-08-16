import json

data={}

def dis_data(dis, data1):
    data_list=[]
    print("\n",dis,"District Details")

    print("<======================================================>\n")

    print("\nUniversal Blood Count :\n")
    contact=data1[0]["others"][0]["for_blood_contact"]
    print(" Contact:", contact)

    #blood_grp=["A_positive", "A_negative", "B_positive", "B_negative", "O_positive", "O_negative", "AB_positive", "AB_negative"]
    data=data1[0]["others"][0]["blood_count"][0]
    blood_grp=list(data)

    blood={}

    for x,c in enumerate(data):
        i=blood_grp[x]
        blood[i]=data[i]
    
    print(blood)

    data_list.append(blood)
    data_list.append(contact)

    #here to access blood_count use data[blood_grp[index]]

    print("<======================================================>\n")

    print("Air Quality: \n")
    aqi=data1[0]["others"][0]["average_air_quality"]

    if aqi >= 0 and aqi <=50:
        condition="Excellent"
        percentage=90
    elif aqi >= 51 and aqi <=100:
        condition="Good"
        percentage=76
    elif aqi >= 101 and aqi <=150:
        condition="Lightly Polluted"
        percentage=65
    elif aqi >= 151 and aqi <=200:
        condition="Moderately Polluted"
        percentage=45
    elif aqi >= 201 and aqi <=300:
        condition="Heavily Polluted"
        percentage=30
    else:
        condition="Severely Polluted"
        percentage=12

    print("", condition)
    print("Percentage:", percentage)

    data_list.append(percentage)

    print("<======================================================>\n")

    print("\nAccident details :\n")
    acc_pin={}

    for i in range(len(data1[0][dis])):
        for j in range(len(data1[0][dis][i]["hospital"])):
            for k in range(len(data1[0][dis][i]["hospital"][j]["road_accident"])):
                pin=data1[0][dis][i]["hospital"][j]["road_accident"][k]["accident_pincode"]
                if pin not in list(acc_pin):
                    acc_pin[pin]=1
                else:
                    acc_pin[pin]=acc_pin[pin]+1

    #print(acc_pin)
    total_acc=0

    for x,c in enumerate(acc_pin):
        total_acc=total_acc+acc_pin[c]

    print(" Total Accident:", total_acc)

    top_2=[]

    for x in range(2):
        max=acc_pin[list(acc_pin)[0]]
        high_pin=list(acc_pin)[0]
        for j in acc_pin:
            if acc_pin[j]>max and j not in top_2:
                max=acc_pin[j]
                high_pin=j
        top_2.append(high_pin)

    print(" Major Accident at :", top_2)

    data_list.append(total_acc)

    print("<======================================================>\n")

    print("\nMedical Stock requirement :\n")

    medical_pin=[]
    medical_dict={}

    for l in range(len(data1[0][dis])):
        medical_pin.append(data1[0][dis][l]["pincode_h"])

    #print(medical_pin)

    for c,x in enumerate(medical_pin):
        med=[]
        for l in range(len(data1[0][dis][c]["medicals"])):
            med_det={}
            med_det['medical']=data1[0][dis][c]["medicals"][l]["medical_name"]
            med_det['owner']=data1[0][dis][c]["medicals"][l]["owner"]
            med_det['phone']=data1[0][dis][c]["medicals"][l]["phone"]
            med_det['email']=data1[0][dis][c]["medicals"][l]["email"]
            med.append(med_det)
        medical_dict[x]=med

    #print(medical_dict)

    pes_dict={}

    for i in range(len(data1[0][dis])):
        pes={}
        for j in range(len(data1[0][dis][i]["hospital"])):
            for k in range(len(data1[0][dis][i]["hospital"][j]["doctors"])):
                for l in range(len(data1[0][dis][i]["hospital"][j]["doctors"][k]["Patient"])):
                    for m in range(len(data1[0][dis][i]["hospital"][j]["doctors"][k]["Patient"][l])):
                        for o in range(len(data1[0][dis][i]["hospital"][j]["doctors"][k]["Patient"][l]["current_illness"])):
                            for p in range(len(data1[0][dis][i]["hospital"][j]["doctors"][k]["Patient"][l]["current_illness"][o]["Drug"])):
                                if data1[0][dis][i]["hospital"][j]["doctors"][k]["Patient"][l]["current_illness"][o]["Drug"][p]["drug_name"] not in list(pes):
                                    pes[data1[0][dis][i]["hospital"][j]["doctors"][k]["Patient"][l]["current_illness"][o]["Drug"][p]["drug_name"]]=1
                                else:
                                    x=data1[0][dis][i]["hospital"][j]["doctors"][k]["Patient"][l]["current_illness"][o]["Drug"][p]["drug_name"]
                                    pes[x]=pes[x]+1
        pes_dict[medical_pin[i]]=pes

    for i in medical_pin:
        print("", i, ":", medical_dict[i], "\n", pes_dict[i], "\n")

    data_list.append(medical_pin)
    data_list.append(medical_dict)
    data_list.append(pes_dict)
    
    print("<======================================================>\n")

    print("\nIllnesses Stats and Camp requirement :\n")

    illness_dict={}

    for i in range(len(data1[0][dis])):
        illness={}
        for j in range(len(data1[0][dis][i]["hospital"])):
            for k in range(len(data1[0][dis][i]["hospital"][j]["doctors"])):
                for l in range(len(data1[0][dis][i]["hospital"][j]["doctors"][k]["Patient"])):
                    for m in range(len(data1[0][dis][i]["hospital"][j]["doctors"][k]["Patient"][l])):
                        for o in range(len(data1[0][dis][i]["hospital"][j]["doctors"][k]["Patient"][l]["current_illness"])):
                            if data1[0][dis][i]["hospital"][j]["doctors"][k]["Patient"][l]["current_illness"][o]["illness"] not in list(illness):
                                illness[data1[0][dis][i]["hospital"][j]["doctors"][k]["Patient"][l]["current_illness"][o]["illness"]]=1
                            else:
                                x=data1[0][dis][i]["hospital"][j]["doctors"][k]["Patient"][l]["current_illness"][o]["illness"]
                                illness[x]=illness[x]+1
        illness_dict[dis]=illness

    print("", illness_dict)

    camp=[]

    for x in range(3):
        max_ill=illness[list(illness)[0]]
        high_ill=list(illness)[0]
        for j in illness:
            if illness[j]>max_ill and j not in camp:
                max_ill=illness[j]
                high_ill=j
        camp.append(high_ill)

    print("\n Top 3 diseases recommended for Awareness CAMP: ", camp, "\n")

    data_list.append(illness)
    data_list.append(camp)

    print("\n<======================================================>")
    print("<======================================================>\n")

    return data_list

district=["static/java/Ahmednagar","static/java/Akola","static/java/Amravati","static/java/Aurangabad","static/java/Beed","static/java/Bhandara","static/java/Buldhana","static/java/Chandrapur","static/java/Dhule","static/java/Gadchiroli","static/java/Gondia","static/java/Hingoli","static/java/Jalgaon","static/java/Jalna","static/java/Kolhapur","static/java/Latur","static/java/Mumbai"]
for d in district:
    link=d+'.json'
    json_data = open(link)  
    # data1 = json_data 
    data1 = json.load(json_data)
    data[d.split("static/java/")[1]]=dis_data(d.split("static/java/")[1], data1)
    print(d.split("static/java/")[1])
    json_data.close()

mumbai_air = data["Mumbai"][2]
Ahmednagar_air = data["Ahmednagar"][2]
Akola_air = data["Akola"][2]
Amravati_air = data["Amravati"][2]
Aurangabad_air = data["Aurangabad"][2]
Beed_air = data["Beed"][2]
Bhandara_air = data["Bhandara"][2]
Buldhana_air = data["Buldhana"][2]
Chandrapur_air = data["Chandrapur"][2]
Dhule_air = data["Dhule"][2]
Gadchiroli_air = data["Gadchiroli"][2]
Gondia_air = data["Gondia"][2]
Hingoli_air = data["Hingoli"][2]
Jalgaon_air = data["Jalgaon"][2]
Jalna_air = data["Jalna"][2]
Kolhapur_air = data["Kolhapur"][2]
Latur_air = data["Latur"][2]


mumbai_acc = data["Mumbai"][3]
Ahmednagar_acc = data["Ahmednagar"][3]
Akola_acc = data["Akola"][3]
Amravati_acc = data["Amravati"][3]
Aurangabad_acc = data["Aurangabad"][3]
Beed_acc = data["Beed"][3]
Bhandara_acc = data["Bhandara"][3]
Buldhana_acc = data["Buldhana"][3]
Chandrapur_acc = data["Chandrapur"][3]
Dhule_acc = data["Dhule"][3]
Gadchiroli_acc = data["Gadchiroli"][3]
Gondia_acc = data["Gondia"][3]
Hingoli_acc = data["Hingoli"][3]
Jalgaon_acc = data["Jalgaon"][3]
Jalna_acc = data["Jalna"][3]
Kolhapur_acc = data["Kolhapur"][3]
Latur_acc = data["Latur"][3]

mumbai_ill = data["Mumbai"][7]
Ahmednagar_ill = data["Ahmednagar"][7]
Akola_ill = data["Akola"][7]
Amravati_ill = data["Amravati"][7]
Aurangabad_ill = data["Aurangabad"][7]
Beed_ill = data["Beed"][7]
Bhandara_ill = data["Bhandara"][7]
Buldhana_ill = data["Buldhana"][7]
Chandrapur_ill = data["Chandrapur"][7]
Dhule_ill = data["Dhule"][7]
Gadchiroli_ill = data["Gadchiroli"][7]
Gondia_ill = data["Gondia"][7]
Hingoli_ill = data["Hingoli"][7]
Jalgaon_ill = data["Jalgaon"][7]
Jalna_ill = data["Jalna"][7]
Kolhapur_ill = data["Kolhapur"][7]
Latur_ill = data["Latur"][7]


MumbaiAp= data["Mumbai"][0]["A_positive"]
MumbaiAn= data["Mumbai"][0]["A_negative"]
MumbaiBp= data["Mumbai"][0]["B_positive"]
MumbaiBn= data["Mumbai"][0]["B_negative"]
MumbaiOp= data["Mumbai"][0]["O_positive"]
MumbaiOn= data["Mumbai"][0]["O_negative"]
MumbaiABp= data["Mumbai"][0]["AB_positive"]
MumbaiABn= data["Mumbai"][0]["AB_negative"]
AhmednagarAp= data["Ahmednagar"][0]["A_positive"]
AhmednagarAn= data["Ahmednagar"][0]["A_negative"]
AhmednagarBp= data["Ahmednagar"][0]["B_positive"]
AhmednagarBn= data["Ahmednagar"][0]["B_negative"]
AhmednagarOp= data["Ahmednagar"][0]["O_positive"]
AhmednagarOn= data["Ahmednagar"][0]["O_negative"]
AhmednagarABp= data["Ahmednagar"][0]["AB_positive"]
AhmednagarABn= data["Ahmednagar"][0]["AB_negative"]
AkolaAp= data["Akola"][0]["A_positive"]
AkolaAn= data["Akola"][0]["A_negative"]
AkolaBp= data["Akola"][0]["B_positive"]
AkolaBn= data["Akola"][0]["B_negative"]
AkolaOp= data["Akola"][0]["O_positive"]
AkolaOn= data["Akola"][0]["O_negative"]
AkolaABp= data["Akola"][0]["AB_positive"]
AkolaABn= data["Akola"][0]["AB_negative"]
AmravatiAp= data["Amravati"][0]["A_positive"]
AmravatiAn= data["Amravati"][0]["A_negative"]
AmravatiBp= data["Amravati"][0]["B_positive"]
AmravatiBn= data["Amravati"][0]["B_negative"]
AmravatiOp= data["Amravati"][0]["O_positive"]
AmravatiOn= data["Amravati"][0]["O_negative"]
AmravatiABp= data["Amravati"][0]["AB_positive"]
AmravatiABn= data["Amravati"][0]["AB_negative"]

AurangabadAp= data["Aurangabad"][0]["A_positive"]
AurangabadAn= data["Aurangabad"][0]["A_negative"]
AurangabadBp= data["Aurangabad"][0]["B_positive"]
AurangabadBn= data["Aurangabad"][0]["B_negative"]
AurangabadOp= data["Aurangabad"][0]["O_positive"]
AurangabadOn= data["Aurangabad"][0]["O_negative"]
AurangabadABp= data["Aurangabad"][0]["AB_positive"]
AurangabadABn= data["Aurangabad"][0]["AB_negative"]
BeedAp= data["Beed"][0]["A_positive"]
BeedAn= data["Beed"][0]["A_negative"]
BeedBp= data["Beed"][0]["B_positive"]
BeedBn= data["Beed"][0]["B_negative"]
BeedOp= data["Beed"][0]["O_positive"]
BeedOn= data["Beed"][0]["O_negative"]
BeedABp= data["Beed"][0]["AB_positive"]
BeedABn= data["Beed"][0]["AB_negative"]
BeedAp= data["Beed"][0]["A_positive"]
BeedAn= data["Beed"][0]["A_negative"]
BeedBp= data["Beed"][0]["B_positive"]
BeedBn= data["Beed"][0]["B_negative"]
BeedOp= data["Beed"][0]["O_positive"]
BeedOn= data["Beed"][0]["O_negative"]
BeedABp= data["Beed"][0]["AB_positive"]
BeedABn= data["Beed"][0]["AB_negative"]
BhandaraAp= data["Bhandara"][0]["A_positive"]
BhandaraAn= data["Bhandara"][0]["A_negative"]
BhandaraBp= data["Bhandara"][0]["B_positive"]
BhandaraBn= data["Bhandara"][0]["B_negative"]
BhandaraOp= data["Bhandara"][0]["O_positive"]
BhandaraOn= data["Bhandara"][0]["O_negative"]
BhandaraABp= data["Bhandara"][0]["AB_positive"]
BhandaraABn= data["Bhandara"][0]["AB_negative"]
print(data["Mumbai"][0])
# print(data["Mumbai"][2])



