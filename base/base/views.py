from django.http import HttpResponse
from django.shortcuts import render
# from Final3 import mumbai_air
from . import Final3

mumbai_air = Final3.mumbai_air
ahmednagar_air = Final3.Ahmednagar_air
akola_air = Final3.Akola_air
amravati_air = Final3.Amravati_air
aurangabad_air = Final3.Aurangabad_air
beed_air = Final3.Beed_air
bhandara_air = Final3.Bhandara_air
buldhana_air = Final3.Buldhana_air
chandrapur_air = Final3.Chandrapur_air
dhule_air = Final3.Dhule_air
gadchiroli_air = Final3.Gadchiroli_air
gondia_air = Final3.Gondia_air
hingoli_air = Final3.Hingoli_air
jalgaon_air = Final3.Jalgaon_air
jalna_air = Final3.Jalna_air
kolhapur_air = Final3.Kolhapur_air
latur_air = Final3.Latur_air

mumbai_acc = Final3.mumbai_acc
ahmednagar_acc = Final3.Ahmednagar_acc
akola_acc = Final3.Akola_acc
amravati_acc = Final3.Amravati_acc
aurangabad_acc = Final3.Aurangabad_acc
beed_acc = Final3.Beed_acc
bhandara_acc = Final3.Bhandara_acc
buldhana_acc = Final3.Buldhana_acc
chandrapur_acc = Final3.Chandrapur_acc
dhule_acc = Final3.Dhule_acc
gadchiroli_acc = Final3.Gadchiroli_acc
gondia_acc = Final3.Gondia_acc
hingoli_acc = Final3.Hingoli_acc
jalgaon_acc = Final3.Jalgaon_acc
jalna_acc = Final3.Jalna_acc
kolhapur_acc = Final3.Kolhapur_acc
latur_acc = Final3.Latur_acc



MumbaiAp=Final3.MumbaiAp
MumbaiAn=Final3.MumbaiAn
MumbaiBp=Final3.MumbaiBp
MumbaiBn=Final3.MumbaiBn
MumbaiOp=Final3.MumbaiOp
MumbaiOn=Final3.MumbaiOn
MumbaiABp=Final3.MumbaiABp
MumbaiABn=Final3.MumbaiABn
AhmednagarAp=Final3.AhmednagarAp
AhmednagarAn=Final3.AhmednagarAn
AhmednagarBp=Final3.AhmednagarBp
AhmednagarBn=Final3.AhmednagarBn
AhmednagarOp=Final3.AhmednagarOp
AhmednagarOn=Final3.AhmednagarOn
AhmednagarABp=Final3.AhmednagarABp
AhmednagarABn=Final3.AhmednagarABn
AkolaAp=Final3.AkolaAp
AkolaAn=Final3.AkolaAn
AkolaBp=Final3.AkolaBp
AkolaBn=Final3.AkolaBn
AkolaOp=Final3.AkolaOp
AkolaOn=Final3.AkolaOn
AkolaABp=Final3.AkolaABp
AkolaABn=Final3.AkolaABn


params = {'Mumbai_air':mumbai_air, "ahmednagar_air":ahmednagar_air, 'akola_air':akola_air, 
'amravati_air':amravati_air, 'aurangabad_air':aurangabad_air, 'beed_air':beed_air, 
'bhandara_air':bhandara_air, 'buldhana_air':buldhana_air, 'chandrapur_air':chandrapur_air, 'dhule_air':dhule_air
,'gadchiroli_air':gadchiroli_air, 'gondia_air':gondia_air, 'hingoli_air':hingoli_air, 'jalgaon_air':jalgaon_air,
'jalna_air':jalna_air, 'kolhapur_air':kolhapur_air, 'latur_air':latur_air, 'Mumbai_acc':mumbai_acc, "ahmednagar_acc":ahmednagar_acc, 'akola_acc':akola_acc, 
'amravati_acc':amravati_acc, 'aurangabad_acc':aurangabad_acc, 'beed_acc':beed_acc, 
'bhandara_acc':bhandara_acc, 'buldhana_acc':buldhana_acc, 'chandrapur_acc':chandrapur_acc, 'dhule_acc':dhule_acc
,'gadchiroli_acc':gadchiroli_acc, 'gondia_acc':gondia_acc, 'hingoli_acc':hingoli_acc, 'jalgaon_acc':jalgaon_acc,
'jalna_acc':jalna_acc, 'kolhapur_acc':kolhapur_acc, 'latur_acc':latur_acc,
'MumbaiAp':MumbaiAp,'MumbaiBp':MumbaiBp,'MumbaiBn':MumbaiBn,'MumbaiOp':MumbaiOp,'MumbaiOn':MumbaiOn,'MumbaiABp':MumbaiABp
, 'MumbaiABn':MumbaiABn, 'AhmednagarAp':AhmednagarAp, 'AhmednagarAn':AhmednagarAn,'AhmednagarBp':AhmednagarBp,'AhmednagarBn':AhmednagarBn
,'AhmednagarOp':AhmednagarOp, 'AhmednagarOn':AhmednagarOn, 'AhmednagarABp':AhmednagarABp, 'AhmednagarABn':AhmednagarABn} 

 
def index(request):
    return render(request, 'maharashtra.html', params)

def stockup(request):
    return render(request, 'chemist.html')

