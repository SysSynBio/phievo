from classes_eds2 import *
from mutation import *
from interaction import *
data=[]
data.append(-13.999942)
data.append(0.000000)
data.append(0.000000)
import random
g=random.Random(42)
L=Mutable_Network(g)
L.Cseed=93042
s0=Species()
s0.activity=1
s0.degradation=0.259188697686
s0.removable=False
s0.n_put=0
s0.mutable=1
s0.order=0
s0.types=['Species', 'Degradable', 'TF', 'Input']
L.add_Node(s0)
s1=Species()
s1.activity=1
s1.degradation=0.192511978482
s1.removable=True
s1.n_put=0
s1.mutable=1
s1.order=1
s1.types=['Species', 'Degradable', 'Phosphorylable', 'TF', 'Complexable', 'Output']
L.add_Node(s1)
n2=CorePromoter()
n2.output=['Species']
n2.delay=81
n2.removable=True
n2.mutable=1
n2.input=['TModule']
n2.order=2
L.add_Node(n2)
n3=TModule()
n3.basal=0.0
n3.rate=0.613995222776
n3.removable=True
n3.mutable=1
n3.order=3
L.add_Node(n3)
n4=TFHill()
n4.input=['TF']
n4.output=['TModule']
n4.hill=3.34542152424
n4.removable=True
n4.activity=1
n4.threshold=0.659134939854
n4.mutable=1
n4.order=7
L.add_Node(n4)
n5=TFHill()
n5.input=['TF']
n5.output=['TModule']
n5.hill=3.81907363105
n5.removable=True
n5.activity=1
n5.threshold=0.185854598105
n5.mutable=1
n5.order=8
L.add_Node(n5)
s2=Species()
s2.activity=0
s2.removable=True
s2.n_put=1
s2.mutable=1
s2.degradation=0.931401784607
s2.order=15
s2.types=['Species', 'Degradable', 'Phosphorylable', 'TF', 'Complexable', 'Output']
L.add_Node(s2)
n7=CorePromoter()
n7.output=['Species']
n7.delay=236
n7.removable=True
n7.mutable=1
n7.input=['TModule']
n7.order=16
L.add_Node(n7)
n8=TModule()
n8.basal=0.0
n8.rate=0.81528989765
n8.removable=True
n8.mutable=1
n8.order=17
L.add_Node(n8)
n9=TFHill()
n9.input=['TF']
n9.output=['TModule']
n9.hill=3.50904933663
n9.removable=True
n9.activity=0
n9.threshold=0.229853875924
n9.mutable=1
n9.order=18
L.add_Node(n9)
n10=TFHill()
n10.input=['TF']
n10.output=['TModule']
n10.hill=3.87856352021
n10.removable=True
n10.activity=0
n10.threshold=0.113394736016
n10.mutable=1
n10.order=19
L.add_Node(n10)
n11=TFHill()
n11.input=['TF']
n11.output=['TModule']
n11.hill=1.94569989586
n11.removable=True
n11.activity=1
n11.threshold=0.14828755941
n11.mutable=1
n11.order=20
L.add_Node(n11)
s3=Species()
s3.degradation=0.930873284482
s3.removable=True
s3.activity=0
s3.mutable=1
s3.order=23
s3.types=['Species', 'Degradable', 'Phosphorylable', 'TF', 'Complexable']
L.add_Node(s3)
n13=CorePromoter()
n13.output=['Species']
n13.delay=146
n13.removable=True
n13.mutable=1
n13.input=['TModule']
n13.order=24
L.add_Node(n13)
n14=TModule()
n14.basal=0.0
n14.rate=0.652251609705
n14.removable=True
n14.mutable=1
n14.order=25
L.add_Node(n14)
n15=TFHill()
n15.input=['TF']
n15.output=['TModule']
n15.hill=3.07323633324
n15.removable=True
n15.activity=1
n15.threshold=0.372878074615
n15.mutable=1
n15.order=29
L.add_Node(n15)
n16=TFHill()
n16.input=['TF']
n16.output=['TModule']
n16.hill=0.787212983971
n16.removable=True
n16.activity=0
n16.threshold=0.316660174297
n16.mutable=1
n16.order=30
L.add_Node(n16)
n17=TFHill()
n17.input=['TF']
n17.output=['TModule']
n17.hill=2.89309377667
n17.removable=True
n17.activity=1
n17.threshold=0.00845660963438
n17.mutable=1
n17.order=31
L.add_Node(n17)
L.activator_required=1
L.fixed_activity_for_TF=0
L.graph.add_edge(s0,n5)
L.graph.add_edge(s0,n11)
L.graph.add_edge(s0,n17)
L.graph.add_edge(s1,n4)
L.graph.add_edge(s1,n15)
L.graph.add_edge(n2,s1)
L.graph.add_edge(n3,n2)
L.graph.add_edge(n4,n3)
L.graph.add_edge(n5,n3)
L.graph.add_edge(s2,n9)
L.graph.add_edge(s2,n10)
L.graph.add_edge(s2,n16)
L.graph.add_edge(n7,s2)
L.graph.add_edge(n8,n7)
L.graph.add_edge(n9,n8)
L.graph.add_edge(n10,n3)
L.graph.add_edge(n11,n8)
L.graph.add_edge(n13,s3)
L.graph.add_edge(n14,n13)
L.graph.add_edge(n15,n14)
L.graph.add_edge(n16,n14)
L.graph.add_edge(n17,n14)