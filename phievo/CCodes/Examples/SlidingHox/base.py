from classes_eds2 import *
from mutation import *
from interaction import *
data=[]
data.append(-0.634732)
data.append(0.000000)
data.append(0.000000)
import random
g=random.Random(42)
L=Mutable_Network(g)
L.Cseed=78242
s0=Species()
s0.order=0
s0.activity=1
s0.n_put=0
s0.degradation=0.66491545339
s0.types=['Species', 'Degradable', 'TF', 'Input']
L.add_Node(s0)
s1=Species()
s1.order=1
s1.activity=1
s1.n_put=0
s1.degradation=0.170884223688
s1.types=['Species', 'Degradable', 'Phosphorylable', 'TF', 'Complexable', 'Output']
L.add_Node(s1)
n2=CorePromoter()
n2.delay=0
n2.output=['Species']
n2.input=['TModule']
n2.order=2
L.add_Node(n2)
n3=TModule()
n3.basal=0.0
n3.rate=0.402820780457
n3.order=3
L.add_Node(n3)
s2=Species()
s2.order=4
s2.activity=1
s2.n_put=1
s2.degradation=0.233007650389
s2.types=['Species', 'Degradable', 'Phosphorylable', 'TF', 'Complexable', 'Output']
L.add_Node(s2)
n5=CorePromoter()
n5.delay=0
n5.output=['Species']
n5.input=['TModule']
n5.order=5
L.add_Node(n5)
n6=TModule()
n6.basal=0.0
n6.rate=0.927521364853
n6.order=6
L.add_Node(n6)
s3=Species()
s3.activity=1
s3.order=7
s3.types=['Species', 'Degradable', 'Phosphorylable', 'TF', 'Complexable']
s3.degradation=0.100453159448
L.add_Node(s3)
n8=CorePromoter()
n8.delay=0
n8.output=['Species']
n8.input=['TModule']
n8.order=8
L.add_Node(n8)
n9=TModule()
n9.basal=0.0
n9.rate=0.0708373600588
n9.order=9
L.add_Node(n9)
n10=TFHill()
n10.output=['TModule']
n10.hill=3.40909957235
n10.activity=1
n10.threshold=0.276928156746
n10.input=['TF']
n10.order=10
L.add_Node(n10)
n11=TFHill()
n11.output=['TModule']
n11.hill=2.19659715213
n11.activity=1
n11.threshold=0.211495919598
n11.input=['TF']
n11.order=11
L.add_Node(n11)
n12=TFHill()
n12.output=['TModule']
n12.hill=4.19242696936
n12.activity=0
n12.threshold=0.978817483205
n12.input=['TF']
n12.order=12
L.add_Node(n12)
n13=TFHill()
n13.output=['TModule']
n13.hill=4.75322187519
n13.activity=1
n13.threshold=0.920494007592
n13.input=['TF']
n13.order=13
L.add_Node(n13)
n14=TFHill()
n14.output=['TModule']
n14.hill=2.4258585834
n14.activity=1
n14.threshold=0.792474617299
n14.input=['TF']
n14.order=14
L.add_Node(n14)
n15=TFHill()
n15.output=['TModule']
n15.hill=4.48289183704
n15.activity=1
n15.threshold=0.725584829737
n15.input=['TF']
n15.order=15
L.add_Node(n15)
L.activator_required=1
L.noise_level=1
L.fixed_activity_for_TF=0
L.graph.add_edge(s0,n13)
L.graph.add_edge(s0,n14)
L.graph.add_edge(s1,n10)
L.graph.add_edge(s1,n12)
L.graph.add_edge(n2,s1)
L.graph.add_edge(n3,n2)
L.graph.add_edge(s2,n11)
L.graph.add_edge(n5,s2)
L.graph.add_edge(n6,n5)
L.graph.add_edge(s3,n15)
L.graph.add_edge(n8,s3)
L.graph.add_edge(n9,n8)
L.graph.add_edge(n10,n3)
L.graph.add_edge(n11,n6)
L.graph.add_edge(n12,n6)
L.graph.add_edge(n13,n9)
L.graph.add_edge(n14,n6)
L.graph.add_edge(n15,n3)

L.write_id()