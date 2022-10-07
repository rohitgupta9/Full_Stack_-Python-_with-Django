def myFun(**kwargs):
    	for key, value in kwargs.items():
		    print("%s == %s" % (key, value))



myFun(first='I', mid='Love', last='iNeuron Platform')
