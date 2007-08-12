TDS={0:time.time()};
ADL={};
def ados(source,body):
 source=source[0];
 if TDS[0]+30<time.time():
  ADL.clear();
  TDS[0]=time.time();
 if not ADL.has_key(source): ADL[source]=0;
 ADL[source]+=1;
 return ADL[source]<15;